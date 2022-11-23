from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, "CTFLog/login.html")

    else:
        if not request.POST["email"] or request.POST["password"]:
            raise ValueError

        user = authenticate(email=request.POST["email"], password=request.POST["password"])
        if user is not None:
            # A backend authenticated the credentials
            return render(request, "CTFLog/index.html")
        else:
            # No backend authenticated the credentials
            raise ValueError

@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "GET":
        return render(request, "CTFLog/register.html")

    else:
        if not request.POST["email"] or request.POST["password"] or request.POST["password_confirm"]:
            raise ValueError

        if request.POST["password"] != request.POST["password_confirm"]:
            raise ValueError

        user = authenticate(email=request.POST["email"], password=request.POST["password"])
        if user is not None:
            # A backend authenticated the credentials
            return render(request, "CTFLog/index.html")
        else:
            # No backend authenticated the credentials
            raise ValueError
