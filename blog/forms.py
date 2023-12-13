from django import forms

from .models import Article, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("author", "category", "topic", "body", "posted", "thumbnail")
