from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_post = models.IntegerField(verbose_name="total posts", default=0)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    posted = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to="thumbnails/", default="default.jpg", null=True, blank=True
    )
    slug = models.SlugField(max_length=80, null=True, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.created_on is None and self.posted:
            self.created_on = timezone.now()

        if self.created_on:
            self.updated_on = timezone.now()

        if not self.slug:
            self.slug = slugify(self.topic)

        if not self.pk and self.category is not None:
            self.category.total_post += 1

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("blog:article_details", kwargs={"slug": self.slug})
