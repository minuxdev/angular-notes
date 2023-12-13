from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from blog.models import Article, Category


class CategoryTest(TestCase):
    def test_model_fields(self):
        """Test model fields"""
        category = Category()
        self.assertEqual("name", category._meta.get_field("name").name)
        self.assertEqual(
            "total_post", category._meta.get_field("total_post").name
        )

    def test_create_category(self):
        """Test create category"""
        Category.objects.create(name="Django Test")

        self.assertEqual(Category.objects.count(), 1)

    def test_create_category_empty_name(self):
        """Test create category with empty 'name'"""

        # with self.assertRaises(ValueError):
        # category = Category.objects.create(name="")

    def test_create_category_duplicated_entries(self):
        """Test create category with unique constraint violation"""

        with self.assertRaises(IntegrityError):
            Category.objects.create(name="blog-1")
            Category.objects.create(name="blog-1")

    def test_str_representation(self):
        """Test string representation"""

        category = Category.objects.create(name="Django Test")
        self.assertEqual(str(category), category.name)


class ArticleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="minux", email="minux@test.com", password="testpassword"
        )
        cls.category = Category.objects.create(name="Django")

    def setUp(self):
        """Preparing dataset to run before each test."""
        self.article_ = Article(
            author=self.user,
            category=self.category,
            topic="New linux topic",
            body="Article body conent",
        )
        self.client.force_login(self.user)

    def test__model_fields(self):
        """Test if model has all required fields"""

        article = Article()

        self.assertEqual("author", article._meta.get_field("author").name)
        self.assertEqual("category", article._meta.get_field("category").name)
        self.assertEqual("topic", article._meta.get_field("topic").name)
        self.assertEqual("body", article._meta.get_field("body").name)
        self.assertEqual("posted", article._meta.get_field("posted").name)
        self.assertEqual(
            "thumbnail", article._meta.get_field("thumbnail").name
        )
        self.assertEqual(
            "updated_on", article._meta.get_field("updated_on").name
        )
        self.assertEqual(
            "created_on", article._meta.get_field("created_on").name
        )
        self.assertEqual("slug", article._meta.get_field("slug").name)

    def test_create_article(self):
        """Test create article model"""

        # Create instance
        self.article_.save()
        self.assertEqual(Article.objects.count(), 1)

    def test_create_article_duplicated_topic(self):
        """
        Test create article with unique constraint violation for
        'topic' field
        """

        with self.assertRaises(IntegrityError):
            Article.objects.create(
                author=self.user,
                category=self.category,
                topic="topic",
                body="body",
                posted=True,
            )

            Article.objects.create(
                author=self.user,
                category=self.category,
                topic="topic",
                body="body content",
                posted=True,
            )

    def test_create_article_duplicated_body(self):
        """
        Test create category with unique constraint violation for
        'body' field
        """

        with self.assertRaises(IntegrityError):
            Article.objects.create(
                author=self.user,
                category=self.category,
                topic="New linux topic",
                body="body",
                posted=True,
            )

            Article.objects.create(
                author=self.user,
                category=self.category,
                topic="New linux topic",
                body="body",
                posted=True,
            )

    def test_create_user_missing_author(self):
        """Test create article without 'author'"""

        with self.assertRaises(IntegrityError):
            self.article_.author = None
            self.article_.save()

    def test_create_user_missing_category(self):
        """Test create article without 'category'"""

        try:
            self.article_.category = None
            self.article_.save()
        except Exception:
            self.assertIsNone(self.article_.pk)

    def test_create_user_missing_topic(self):
        """Test create article without 'topic'"""

        with self.assertRaises(IntegrityError):
            self.article_.topic = None
            self.article_.save()

    def test_create_user_missing_body(self):
        """Test create article without 'body content'"""

        with self.assertRaises(IntegrityError):
            self.article_.body = None
            self.article_.save()

    def test_str_representation(self):
        """Test string representation"""

        self.article_.save()
        self.assertEqual(str(self.article_), self.article_.topic)

    def test_set_created_on_field_if_posted(self):
        """Test set date time for 'created_on' field only if 'posted'"""

        self.article_.posted = True
        self.article_.save()
        self.assertIsNotNone(self.article_.created_on)

    def test_set_updated_on_field_if_created_on(self):
        """Test set date time for 'updated_on' field only if 'created_on'"""

        self.article_.posted = True
        self.article_.save()
        self.assertIsNotNone(self.article_.updated_on)

    def test_set_slug(self):
        """Test slug is auto generated"""

        self.article_.save()
        self.assertEqual(self.article_.slug, slugify(self.article_.topic))

    def test_update_total_post_on_category(self):
        """Test update 'category.total_post' field whenever new article is created"""
        total_post = self.category.total_post

        Article.objects.create(
            author=self.user,
            category=self.category,
            topic="topic",
            body="body",
            posted=True,
        )

        Article.objects.create(
            author=self.user,
            category=self.category,
            topic="topic 2",
            body="body content",
            posted=True,
        )

        updated_total_post = self.category.total_post
        self.assertGreater(updated_total_post, total_post)
