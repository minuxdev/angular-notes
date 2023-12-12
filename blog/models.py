from enum import unique

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_post = models.IntegerField(
        verbose_name="total posts",
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        to=Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    topic = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    posted = models.BooleanField(default=False)
    slug = models.SlugField()
    thumbnail = models.ImageField(
        upload_to="thumbnails/", default="default.jpg", null=True, blank=True
    )
    create_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.topic
