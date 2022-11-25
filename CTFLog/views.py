from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request, template_name="CTFLog/login.html", context={"login_form": form}
    )


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="CTFLog/register.html",
        context={"register_form": form},
    )


@require_safe
@login_required
def index(request):
    return render(request=request, template_name="CTFLog/index.html")


@login_required
def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")
