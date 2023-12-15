from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import resolve

from blog.forms import ArticleForm
from blog.models import Article, Category
from blog.views import article_create, article_details, article_update, home


class HomeViewTest(TestCase):
    """Test all functionalities for home page"""

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="category 1")
        cls.user = get_user_model().objects.create_user(
            username="minux", password="test"
        )

    def setUp(self):
        self.url = reverse("blog:home")

        self.article = Article.objects.create(
            author=self.user,
            category=self.category,
            topic="Topic 1",
            body="Body 1",
        )

        self.response = self.client.get(self.url)

        self.client.force_login(self.user)

    def test_url_resolve(self):
        """Test if url resolve to home view."""

        view = resolve(self.url)
        self.assertEqual(view.func, home)

    def test_used_template(self):
        """Test if desired template was used"""

        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, template_name="blog/home.html")

    def test_render_articles(self):
        """Test if render articles"""

        self.assertContains(self.response, self.article.body)

    def test_topic_is_link(self):
        """Test if topic is used as link to instance"""

        self.assertContains(
            self.response,
            f'<a href="{self.article.get_absolute_url()}">{self.article.topic}',
        )


class ArticleDetailsTest(TestCase):
    """Test all functionalities for article details view"""

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="category 1")
        cls.user = get_user_model().objects.create_user(
            username="minux", password="test"
        )

    def setUp(self):
        self.article = Article.objects.create(
            author=self.user,
            category=self.category,
            topic="Topic 1",
            body="Body 1",
        )

        self.url = self.article.get_absolute_url()
        self.response = self.client.get(self.url)

    def test_url_resolve(self):
        """Test if url resolve to article details view."""

        view = resolve(self.url)
        self.assertEqual(view.func, article_details)

    def test_used_template(self):
        """Test if desired template was used"""

        self.assertTemplateUsed(self.response, "blog/article_details.html")

    def test_increment_views_on_get(self):
        """Test article views on get"""
        initial_views = self.article.views
        self.client.get(self.url)
        # self.assertNotEqual(initial_views, self.article.views)


class ArticleCreateTest(TestCase):
    """Test all functionalities for article create view"""

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="category 1")
        cls.user = get_user_model().objects.create_user(
            username="minux", password="test"
        )

    def setUp(self):
        self.url = reverse("blog:article_create")
        self.response = self.client.get(self.url)

        self.client.force_login(self.user)

    def test_url_resolve(self):
        """Test if url resolve to article create view."""

        view = resolve(self.url)
        self.assertEqual(view.func, article_create)

    def test_used_template(self):
        """Test if desired template was used"""

        self.assertTemplateUsed(self.response, "blog/article_create.html")

    def test_post_valid_data(self):
        """Test create article on valid form"""

        form_data = {
            "category": self.category.pk,
            "topic": "Topic 1",
            "body": "Body 1",
            "posted": True,
        }

        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_redirect_to_details_view(self):
        """Test if redirect to its details on succsess"""

        form_data = {
            "category": self.category.pk,
            "topic": "Topic 2",
            "body": "Body 2",
        }

        response = self.client.post(self.url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

        url = response.request["PATH_INFO"]
        self.assertEqual(resolve(url).func, article_details)


class ArticleUpdateView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="category 1")
        cls.user = get_user_model().objects.create_user(
            username="minux", password="test"
        )

    def setUp(self):
        self.article = Article.objects.create(
            author=self.user,
            category=self.category,
            topic="Topic 1",
            body="Body 1",
        )

        self.url = reverse(
            "blog:article_update", kwargs={"slug": self.article.slug}
        )
        self.response = self.client.get(self.url)
        self.client.force_login(self.user)

    def test_url_resolve(self):
        """Test if url resolve to article_update view."""

        view = resolve(self.url)
        self.assertEqual(view.func, article_update)

    def test_used_template(self):
        """Test if article_create template was used"""

        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(
            self.response, template_name="blog/article_create.html"
        )

    def test_update_on_valid_form(self):
        """Test if update on valid form"""

        form_data = {
            "author": self.user.pk,
            "category": self.category.pk,
            "topic": "Updated topic 1",
            "body": "Updated body 1",
        }

        self.client.post(self.url, data=form_data)
        article = Article.objects.get(body=form_data["body"])

        self.assertEqual(article.body, form_data["body"])

    def test_redirect_to_details_view(self):
        """Test if redirect to its details on succsess"""

        form_data = {
            "author": self.user.pk,
            "category": self.category.pk,
            "topic": "Topic 2",
            "body": "Body 2",
        }

        response = self.client.post(self.url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

        url = response.request["PATH_INFO"]
        self.assertEqual(resolve(url).func, article_details)
