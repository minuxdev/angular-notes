from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from blog.forms import ArticleForm, CategoryForm
from blog.models import Article, Category


def get_article(slug):
    return Article.objects.get(slug=slug)


def construct_pagination(request, obj, per_page):
    paginator = Paginator(obj, per_page)
    page_number = request.GET.get("page", 1)
    return paginator.get_page(page_number)


def home(request):
    if request.method == "POST":
        query = request.POST["query"]
        articles = Article.articles.filter(
            Q(topic__icontains=query) | Q(body__icontains=query)
        )
    else:
        articles = Article.articles.all()

    if request.user.is_authenticated:
        articles = articles.filter(author=request.user)

    page_obj = construct_pagination(request, articles, 6)

    context = {"articles": articles, "page_obj": page_obj}
    return render(request, "blog/home.html", context)


@transaction.atomic()
def article_details(request, slug):
    article = get_article(slug)
    id_ = article.pk

    instance_id = request.session.get(f"instance_{id_}", 0)
    if instance_id != article.pk:
        article.views += 1
        article.save()
        request.session[f"instance_{id_}"] = article.pk

    related_articles = Article.objects.all().exclude(slug=slug)[:6]
    context = {"article": article, "related_articles": related_articles}
    return render(request, "blog/article_details.html", context=context)


def get_category(pk):
    return Category.objects.get(pk=pk)


def categories(request):
    if request.user.is_authenticated:
        categories = Category.objects.filter(
            author=request.user, total_post__gt=0
        )
    else:
        categories = Category.objects.filter(total_post__gt=0)
    page_obj = construct_pagination(request, categories, 6)
    context = {"page_obj": page_obj}
    return render(request, "blog/categories.html", context)


def category_details(request, pk):
    instance = get_category(pk)
    articles = instance.article.all()
    page_obj = construct_pagination(request, articles, 8)
    context = {
        "instance": instance,
        "page_obj": page_obj,
    }
    return render(request, "blog/category_details.html", context)


# Management
@login_required()
def category_create(request):
    form = CategoryForm()
    if request.method == "POST":
        if form.is_valid():
            author = request.user
            name = request.POST.get("name")
            category = Category.objects.get_or_create(name=name, author=author)
            return redirect(reverse("dashboard"))
    return render(request, "blog/category_create.html", {"form": form})


@login_required()
def category_update(request, pk):
    category = get_category(pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect(f"{reverse('blog:dashboard')}?q=categories")
    return render(request, "blog/category_create.html", {"form": form})


@login_required()
def category_delete(request, pk):
    category = get_category(pk)
    return HttpResponse(category)


@login_required()
def article_create(request):
    form = ArticleForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.thumbnail = request.POST.get("thumbnail")
            article.save()
            messages.success(request, "You data was saved successfully!")
            print(article.thumbnail)
            return redirect(article.get_absolute_url())
        else:
            print(form.errors)

    return render(request, "blog/article_create.html", {"form": form})


@login_required()
def article_update(request, slug):
    article = get_article(slug)
    print(article.thumbnail)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        if request.FILES:
            thumbnail = request.FILES.get("thumbnail", None)
            instance.thumbnail = image_uploader(thumbnail)
            print(instance.thumbnail)
        instance.save()
        # messages.success(request, "You data was saved successfully!")
        return redirect(f"{reverse('blog:dashboard')}?q=articles")

    context = {"form": form}
    return render(request, "blog/article_create.html", context)


@login_required()
def article_delete(request, slug):
    article = get_article(slug)
    article.delete()
    return redirect("blog:dashboard")


@login_required()
def dashboard(request):
    query = request.GET.get("q", None)
    if query == "categories":
        obj = Category.objects.filter(author=request.user)
    else:
        obj = Article.objects.filter(author=request.user)

    recent_obj = obj[:6]
    page_obj = construct_pagination(request, obj, 6)
    context = {"page_obj": page_obj, "query": query, "recent_obj": recent_obj}
    return render(request, "blog/dashboard.html", context)
