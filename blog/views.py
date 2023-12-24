from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import redirect, render

from blog.forms import ArticleForm
from blog.models import Article


def home(request):
    if request.method == "POST":
        query = request.POST["query"]
        articles = Article.objects.filter(
            Q(topic__icontains=query) | Q(body__icontains=query)
        )
    else:
        articles = Article.objects.all()

    return render(request, "blog/home.html", context={"articles": articles})


def get_article(slug):
    return Article.objects.get(slug=slug)


@login_required()
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


# Management
@login_required()
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect(article.get_absolute_url())

    form = ArticleForm()
    return render(request, "blog/article_create.html", {"form": form})


@login_required()
def article_update(request, slug):
    article = get_article(slug)
    form = ArticleForm(data=request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect(article.get_absolute_url())

    context = {"form": form}
    return render(request, "blog/article_create.html", context)


@login_required()
def article_delete(request, slug):
    article = get_article(slug)
    article.delete()
    return redirect("blog:dashboard")


@login_required()
def dashboard(request):
    articles = Article.objects.all()
    return render(request, "blog/dashboard.html", {"articles": articles})
