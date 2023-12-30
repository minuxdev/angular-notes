from django.contrib.auth import get_user_model
from django.test import TestCase

from users.forms import UserAddForm, UserEditForm, UserLoginForm


class UserAddFormTest(TestCase):
    def test_form_fields(self):
        """Test if UserAddForm has expected fields"""

        form = UserAddForm()
        self.assertIn("email", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)

    def test_valid_form(self):
        """Test valid form"""

        form_data = {
            "email": "email@test.com",
            "password1": "password_newtest",
            "password2": "password_newtest",
        }

        form = UserAddForm(form_data)

        # test if valid data was passed
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        """Test valid form"""

        form_data = {
            "email": "email.com",
            "password1": "password_newtest",
            "password2": "password_newtest",
        }

        form = UserAddForm(form_data)

        # test if invalid data was passed
        self.assertFalse(form.is_valid())

    def test_unmatched_passwords(self):
        """Test unmatched passwords"""

        form_data = {
            "email": "email@test.com",
            "password1": "password_newtest",
            "password2": "password_oldtest",
        }

        form = UserAddForm(form_data)

        # test if invalid data was passed
        self.assertFalse(form.is_valid())

    def test_hashed_password(self):
        """Test if password is hashed on save"""

        form_data = {
            "email": "email@test.com",
            "password1": "password_newtest",
            "password2": "password_newtest",
        }

        form = UserAddForm(form_data)

        # test if invalid data was passed
        self.assertTrue(form.is_valid())

        user = form.save()
        self.assertTrue(user.check_password("password_newtest"))


class UserEditFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            email="email@test.com", password="passwordtest"
        )

    def test_form_fields(self):
        """Test if UserEditForm has expected fields"""

        form = UserEditForm()
        self.assertIn("email", form.fields)
        self.assertIn("password", form.fields)

    def test_edit_email(self):
        """Test edit user email"""
        form_data = {
            "email": "new.email@test.com",
        }
        form = UserEditForm(instance=self.user, data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(self.user.email, "new.email@test.com")

    def test_edit_password(self):
        """Test edit user password"""
        form_data = {
            "email": self.user.email,
            "password": "newpassword",
        }

        form = UserEditForm(instance=self.user, data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # self.assertEqual(self.user.email, "new.email@test.com")


class UserLoginFormTest(TestCase):
    def test_form_has_expected_fields(self):
        """Test if login form has all expected fields."""

        form = UserLoginForm()
        self.assertIn("email", form.fields)
        self.assertIn("password", form.fields)

    def test_invalid_email(self):
        """Test email validator"""

        with self.assertRaises(ValueError):
            form = UserLoginForm(
                {"email": "e@admin.com", "password": "testpassword"}
            )

    def test_short_email(self):
        """Test email is less than ten characters"""

        with self.assertRaises(ValueError):
            form = UserLoginForm(
                {"email": "e@dev.com", "password": "testpassword"}
            )

    def test_invalid_password(self):
        """Test passowrd validator"""

        form = UserLoginForm({"email": "email@dev.com", "password": ""})
        self.assertFalse(form.is_valid())
