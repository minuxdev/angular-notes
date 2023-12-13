from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.forms import ArticleForm, CategoryForm
from blog.models import Category


class CategoryFormTest(TestCase):
    def test_form_fields(self):
        """Test if form has all required fields for category model"""

        form = CategoryForm()
        self.assertIn("name", form.fields)

    def test_valid_form(self):
        """Test if form is valid"""

        form = CategoryForm({"name": "new category"})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if form is invalid"""

        form = CategoryForm({})
        self.assertFalse(form.is_valid())

    def test_empty_name(self):
        """Test empty name"""

        form = CategoryForm({"name": ""})
        self.assertFalse(form.is_valid())

    def test_create_instance_on_valid_form(self):
        """Test if a Category instance is created when form is valid"""
        form = CategoryForm({"name": "new category"})
        form.save()
        self.assertEqual(Category.objects.count(), 1)

    def test_update_instance_on_valid_form(self):
        """Test if a Category instance is updated when form is valid"""
        category = Category.objects.create(name="new category")
        form = CategoryForm({"name": "updated category"}, instance=category)
        form.save()
        self.assertEqual(category.name, form.data["name"])


class ArticleFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user1", password="123test"
        )
        self.category = Category.objects.create(name="Category")
        self.form_data = {
            "author": self.user,
            "category": self.category,
            "topic": "Topic",
            "body": "Body",
        }

    def test_form_fields(self):
        """Test if form has all required fields for Article model"""

        form = ArticleForm()
        self.assertIn("author", form.fields)
        self.assertIn("category", form.fields)
        self.assertIn("topic", form.fields)
        self.assertIn("body", form.fields)
        self.assertIn("thumbnail", form.fields)
        self.assertIn("posted", form.fields)

    def test_valid_form(self):
        """Test if ArticleForm is valid"""

        form = ArticleForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_category(self):
        """Test if form is invalid for category=None"""

        self.form_data["category"] = None
        form = ArticleForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_topic(self):
        """Test if form is invalid for topic=None"""

        self.form_data["topic"] = None
        form = ArticleForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_body(self):
        """Test if form is invalid for body=None"""

        self.form_data["body"] = None
        form = ArticleForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_create_instance_on_valid_form(self):
        """Test if a Article instance is created when form is valid"""

        form = ArticleForm(data=self.form_data)
        obj = form.save()
        self.assertEqual(obj.topic, form.data["topic"])

    def test_update_instance_on_valid_form(self):
        """Test if a Category instance is updated when form is valid"""

        form = ArticleForm(data=self.form_data)
        article = form.save()

        body = article.body

        self.form_data["body"] = "Updated body"

        updated_form = ArticleForm(data=self.form_data, instance=article)
        updated_article = updated_form.save()

        self.assertNotEqual(body, updated_article.body)
