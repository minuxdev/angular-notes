from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.text import gettext_lazy as _

from .models import User


class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if len(str(email)) < 10:
            # Change it to forms.ValidationError
            raise ValueError(_("Email cannot have less than ten characters."))
        return email
