from django.test import TestCase

from blog.forms import CategoryForm
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
