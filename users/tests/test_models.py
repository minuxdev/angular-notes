from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from users.models import User


class UserTest(TestCase):
    def test_create_normal_user(self):
        """Create normal user."""

        user = get_user_model().objects.create_user(
            email="test@user.com", password="passwd"
        )
        self.assertEqual(user.email, "test@user.com")

    def test_normal_user_is_not_staff_superuser(self):
        """Test if normal user is not staff or superuser"""

        user = get_user_model().objects.create_user(
            email="test@user.com", password="passwd"
        )
        # check user is not staff
        self.assertFalse(user.is_staff)

        # check user is not superuser
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Create superuser."""

        user = get_user_model().objects.create_superuser(
            email="test@user.com", password="passwd"
        )
        self.assertEqual(user.email, "test@user.com")

    def test_superuser_is_staff_superuser(self):
        """Test if normal user is not staff or superuser"""

        user = get_user_model().objects.create_superuser(
            email="test@user.com", password="passwd"
        )
        # check user is not staff
        self.assertTrue(user.is_staff)

        # check user is not superuser
        self.assertTrue(user.is_superuser)

    def test_create_user_with_empty_email(self):
        """Create user with empty email raises a TypeError error"""

        with self.assertRaises(TypeError):
            user = get_user_model().objects.create_user(password="test")

    def test_hashed_password(self):
        """Test if password is hashed"""

        user = get_user_model().objects.create_superuser(
            email="test@user.com", password="passwdhashed"
        )
        self.assertTrue(user.check_password("passwdhashed"))

    def test_date_join(self):
        """Test date join"""

        user = get_user_model().objects.create_superuser(
            email="test@user.com", password="passwd"
        )
        self.assertTrue(user.date_join)
