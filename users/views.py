from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, reverse

from .forms import UserAddForm, UserLoginForm


def create_user(request):
    form = UserAddForm()

    if request.method == "POST":
        form = UserAddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login_user"))

    context = {"form": UserAddForm()}
    return render(request, "users/create_user.html", context)


def login_user(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.data["email"], password=form.data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
    context = {"form": form}
    return render(request, "users/login.html", context)


def logout_user(request):
    logout(request)
    return redirect(settings.LOGIN_URL)
