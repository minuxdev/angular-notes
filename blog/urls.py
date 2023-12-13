from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("article/create/", views.article_create, name="article_create"),
    path("article/<slug>/", views.article_details, name="article_details"),
]
