"""CTFLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    login,
    register,
    index,
    logout,
    show_campaign,
    show_ctf,
    show_site,
    create_ctf,
    create_site,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("site/<slug:site_slug>/", show_site, name="show_site"),
    path("campaign/<slug:campaign_slug>/", show_campaign, name="show_campaign"),
    path("ctf/<slug:ctf_slug>/", show_ctf, name="show_ctf"),
    path("create-site/", create_site, name="create_site"),
    path("create-ctf/<slug:campaign_slug>/", create_ctf, name="create_ctf"),
    path(
        "create-ctf/<slug:campaign_slug>/<int:ctf_int>/", create_ctf, name="create_ctf"
    ),
]
