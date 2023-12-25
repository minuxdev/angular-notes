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

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get("thumbnail", False)

        if thumbnail and thumbnail.size > 3 * 1024**2:
            raise forms.ValidationError("Thumbnail cannot exceed 3.0Mb")

        self.cleaned_data["thumbnail"] = thumbnail

        return thumbnail
