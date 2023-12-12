from django.contrib import admin

from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "total_post")
    list_filter = ("name",)
    ordering = (
        "-id",
        "name",
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("author", "category", "topic", "views", "updated_on")
    list_filter = ("author", "category", "topic")
    ordering = ("-updated_on", "-id")
