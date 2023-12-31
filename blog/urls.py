from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("categories/", views.categories, name="category_list"),
    path(
        "categories/details/<pk>/",
        views.category_details,
        name="category_details",
    ),
    path(
        "categories/update/<pk>/",
        views.category_update,
        name="category_update",
    ),
    path(
        "categories/delete/<pk>/",
        views.category_delete,
        name="category_delete",
    ),
    path("article/create/", views.article_create, name="article_create"),
    path(
        "article/update/<slug>/", views.article_update, name="article_update"
    ),
    path(
        "article/details/<slug>/",
        views.article_details,
        name="article_details",
    ),
    path(
        "article/delete/<slug>/",
        views.article_delete,
        name="article_delete",
    ),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
