from django.contrib.auth import views as v
from django.urls import path

from . import views

# app_name = "users"

urlpatterns = [
    path("signup/", views.create_user, name="create_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    # Password handler
    path(
        "reset-password/",
        v.PasswordResetView.as_view(template_name="users/reset_password.html"),
        name="reset_password",
    ),
    path(
        "reset/email/sent/",
        v.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        v.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset-complete/",
        v.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "change-password/",
        v.PasswordChangeView.as_view(
            template_name="users/password_change.html"
        ),
        name="password_change",
    ),
    path(
        "change-password/done/",
        v.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
