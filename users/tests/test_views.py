from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import resolve, reverse

from users.views import create_user, login_user


class CreateViewTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse("create_user")

    def test_url_resolve_create_user_view(self):
        """Test if view exist"""
        view = resolve(self.url)

        # Assert url resolves to the correct function based view.
        self.assertEqual(view.func, create_user)

        # For class based view
        # self.assertEqual(view.func.view_class, CreateUserView)

    def test_create_user_template(self):
        """Test if create user template is reacheable on GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_valid_form(self):
        """Test if instance is created on valid form"""
        form_data = {
            "email": "minux@dev.com",
            "password1": "@Minux8080",
            "password2": "@Minux8080",
        }

        self.client.post(self.url, data=form_data)

        # Check if instance is created
        user = get_user_model().objects.filter(email=form_data["email"])
        self.assertTrue(user.exists())

    def test_invalid_email(self):
        """
        Test if instance is not created on invalid email and error
        messages are returned accordingly
        """
        form_data = {
            "email": "minuxdev.com",
            "password1": "@Minux8080",
            "password2": "@Minux8080",
        }
        response = self.client.post(self.url, data=form_data)

        # Check redirect did not occour
        self.assertEqual(response.status_code, 200)

    def test_unmatch_passwords(self):
        """
        Test if instance is not created on unmatched passwords and error
        messages are returned accordingly
        """
        form_data = {
            "email": "minux@dev.com",
            "password1": "@Minux8080",
            "password2": "@minux8080",
        }
        response = self.client.post(self.url, data=form_data)

        # Check redirect did not occour
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        """Test if user is correctly created"""
        form_data = {
            "email": "minux@dev.com",
            "password1": "@Minux8080",
            "password2": "@Minux8080",
        }

        self.client.post(self.url, data=form_data)

        # Check if instance is created
        user = get_user_model().objects.filter(email=form_data["email"])
        self.assertTrue(user.exists())

    def test_redirect_to_login_user_view(self):
        """Test redirect to 'login_user' view after create instance"""
        form_data = {
            "email": "minux@dev.com",
            "password1": "@Minux8080",
            "password2": "@Minux8080",
        }
        response = self.client.post(self.url, data=form_data, follow=True)

        # Check if response is redirected to 'home'.
        self.assertRedirects(response, expected_url=reverse("login_user"))

        # Check if correct template was used in redict.
        self.assertTemplateUsed(response, template_name="users/login.html")


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            email="minux@dev.com", password="validpassword"
        )

    def setUp(self):
        self.url = reverse("login_user")

    def test_url_resolve_login_user_view(self):
        """Test login view exists"""
        view = resolve(self.url)
        self.assertEqual(view.func, login_user)

    def test_login_template(self):
        """Test login template exist"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, template_name="users/login.html")

    def test_login_invalid_email(self):
        """Login user with invalid email"""
        form_data = {"email": "minuxdev.com", "password": "validpassword"}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_password(self):
        """Login user with invalid password"""
        form_data = {"email": "minux@dev.com", "password": "invalidpassword"}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_login_valid_credentials(self):
        """Login user with valid credentials"""
        form_data = {"email": "minux@dev.com", "password": "validpassword"}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_redirect_to_home(self):
        """Test if redirect to home on success"""

        form_data = {"email": "minux@dev.com", "password": "validpassword"}
        response = self.client.post(self.url, data=form_data, follow=True)
        self.assertRedirects(response, expected_url=reverse("blog:dashboard"))


class PasswordResetTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="minux@dev.com", password="validpassword"
        )
        self.url = reverse("reset_password")
        self.post_response = self.client.post(
            self.url, data={"email": "minux@dev.com"}, follow=True
        )

        self.email = mail.outbox[0]
        splitted_email_body = self.email.body.split("/")
        self.uidb64 = splitted_email_body[5]
        self.token = splitted_email_body[6]

    def test_reset_password_template(self):
        """Test reset password template"""
        response = self.client.get(self.url)

        self.assertTemplateUsed(
            response, template_name="users/reset_password.html"
        )

    def test_reset_password_redirect_to_email_sent(self):
        """Test reset password template"""

        self.assertRedirects(
            self.post_response,
            expected_url=reverse("password_reset_done"),
        )

        self.assertTemplateUsed(
            self.post_response, template_name="users/password_reset_done.html"
        )

    def test_render_expected_template_on_redirect(self):
        """
        Test expected template is rendered on redirect to
        password_reset_done view
        """

        self.assertTemplateUsed(
            self.post_response, template_name="users/password_reset_done.html"
        )

    def test_shown_message(self):
        """Test message shown is as expected"""

        self.assertContains(
            self.post_response, "A Verification link was sent to your email."
        )

    def test_verification_email_sent(self):
        """Test if email was sent"""

        email_msg = "The testserver team"
        self.assertIn(email_msg, self.email.body)

    def test_set_new_password(self):
        """Test set new password"""

        url = reverse(
            "password_reset_confirm",
            kwargs={"uidb64": self.uidb64, "token": self.token},
        )

        new_password = "NewPassword235"

        response = self.client.post(
            url,
            follow=True,
        )

        # Extract redirected page url
        url = response.request["PATH_INFO"]
        response = self.client.post(
            url,
            data={
                "new_password1": new_password,
                "new_password2": new_password,
            },
        )

        self.assertEqual(response.status_code, 302)

        # self.assertTemplateUsed(
        # response, template_name="password_reset_done.html"
        # )

    def test_redirect_to_password_reset_complete(self):
        """Test redirect to password reset complete template"""

        url = reverse(
            "password_reset_confirm",
            kwargs={"uidb64": self.uidb64, "token": self.token},
        )

        new_password = "NewPassword235"

        response = self.client.post(
            url,
            follow=True,
        )

        # Extract redirected page url
        url = response.request["PATH_INFO"]
        response = self.client.post(
            url,
            data={
                "new_password1": new_password,
                "new_password2": new_password,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        # Check redirect to desired page
        self.assertRedirects(
            response, expected_url=reverse("password_reset_complete")
        )

        # Check used template
        self.assertTemplateUsed(
            response, template_name="users/password_reset_complete.html"
        )


class PasswordChangeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="minux@dev.com", password="testPassword"
        )
        self.client.force_login(self.user)

        self.url = reverse("password_change")

    def test_password_change_template(self):
        """Test password change template"""

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        # Check used template
        self.assertTemplateUsed(
            response, template_name="users/password_change.html"
        )

    def test_valid_password_change(self):
        """Test password change success"""

        new_password = "@Anoder#asd!!"

        response = self.client.post(
            self.url,
            data={
                "old_password": "testPassword",
                "new_password1": new_password,
                "new_password2": new_password,
            },
        )

        # Check if redirection occours
        self.assertEqual(response.status_code, 302)

    def test_redirect_to_password_change_done(self):
        """Test redirect to password change done."""

        new_password = "@Anoder#asd!!"

        response = self.client.post(
            self.url,
            data={
                "old_password": "testPassword",
                "new_password1": new_password,
                "new_password2": new_password,
            },
            follow=True,
        )

        self.assertTrue(response.status_code, 200)
        self.assertRedirects(
            response, expected_url=reverse("password_change_done")
        )
        self.assertTemplateUsed(
            response, template_name="users/password_change_done.html"
        )
