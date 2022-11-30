from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Site, Favorite, Campaign, CTF


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
    sites = Site.objects.all()
    favorites = Favorite.objects.all()
    return render(
        request=request,
        template_name="CTFLog/index.html",
        context={"sites": sites, "favorites": favorites},
    )


@login_required
def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


@require_http_methods(["GET", "POST"])
@login_required
def show_site(request, site_slug):
    if request.method == "POST":
        pass
    else:
        sites = Site.objects.all()
        favorites = Favorite.objects.all()
        campaignsite = Site.objects.get(slug=site_slug)
        campaigns = Campaign.objects.filter(site=campaignsite)
        return render(
            request=request,
            template_name="CTFLog/site.html",
            context={
                "sites": sites,
                "favorites": favorites,
                "campaigns": campaigns,
                "campaignsite": campaignsite,
            },
        )


@require_http_methods(["GET", "POST"])
@login_required
def show_campaign(request, campaign_slug):
    if request.method == "POST":
        pass
    else:
        sites = Site.objects.all()
        favorites = Favorite.objects.all()
        ctf_campaign = Campaign.objects.get(slug=campaign_slug)
        ctfs = CTF.objects.filter(campaign=ctf_campaign)
        return render(
            request=request,
            template_name="CTFLog/campaign.html",
            context={
                "sites": sites,
                "favorites": favorites,
                "ctf_campaign": ctf_campaign,
                "ctfs": ctfs,
            },
        )


@require_http_methods(["GET", "POST"])
@login_required
def show_ctf(request, ctf_slug):
    if request.method == "POST":
        # creator = request.user
        # if public in POST
        pass
    else:
        sites = Site.objects.all()
        favorites = Favorite.objects.all()
        ctf = CTF.objects.get(slug=ctf_slug)
        campaign_ctfs = CTF.objects.filter(campaign=ctf.campaign)
        return render(
            request=request,
            template_name="CTFLog/ctf.html",
            context={
                "sites": sites,
                "favorites": favorites,
                "ctf": ctf,
                "campaign_ctfs": campaign_ctfs,
            },
        )
