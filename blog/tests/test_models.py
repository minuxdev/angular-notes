from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from blog.models import Article, Category


class CategoryTest(TestCase):
    def test_create_category(self):
        """Test create category"""
        category = Category.objects.create(name="Django Test")
        print(category)

        self.assertEqual(Category.objects.count(), 1)

    def test_create_category_empty_name(self):
        """Test create category with empty `name`"""

        with self.assertRaises(ValueError):
            Category.objects.create(name="")

    def test_create_category_duplicated_entries(self):
        """Test create category with unique constraint violation"""

        with self.assertRaises(ValueError):
            Category.objects.create(name="blog-1")
            Category.objects.create(name="blog-1")

    def test_str_representation(self):
        """Test string representation"""

        category = Category.objects.create(name="Django Test")
        self.assertEqual(str(category), category.name)
