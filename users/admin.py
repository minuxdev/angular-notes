from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserAddForm, UserEditForm
from .models import User


class CustomUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserAddForm
    ordering = ("email",)
    list_display = ("email", "is_active", "is_staff", "date_join")
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            "Authentication",
            {"classes": "wide", "fields": ("email", "password1", "passwrd2")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
