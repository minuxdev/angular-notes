from django.shortcuts import redirect, render

from blog.forms import ArticleForm
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "blog/home.html", context=context)


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect(article.get_absolute_url())
    form = ArticleForm()
    return render(request, "blog/article_create.html", {"form": form})


def article_details(request, slug):
    article = get_article(slug)
    id_ = article.pk

    instance_id = request.session.get(f"instance_{id_}", 0)
    print("obj_id: ", instance_id)
    if instance_id != article.pk:
        article.views += 1
        article.save()
        print("Visited oject: ", article, "views: ", article.views)
        request.session[f"instance_{id_}"] = article.pk

    context = {"article": article}
    return render(request, "blog/article_details.html", context=context)


def get_article(slug):
    return Article.objects.get(slug=slug)


def article_update(request, slug):
    article = get_article(slug)
    form = ArticleForm(data=request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect(article.get_absolute_url())

    context = {"form": form}
    return render(request, "blog/article_create.html", context)
