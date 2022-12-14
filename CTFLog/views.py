from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Site, Campaign, CTF
from django.http import Http404
from django.db import IntegrityError

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
    sites = Site.objects.all().order_by("name")
    return render(
        request=request,
        template_name="CTFLog/index.html",
        context={"sites": sites},
    )


@login_required
def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


@require_http_methods(["GET", "POST"])
@login_required
def show_site(request, site_slug):
    sites = Site.objects.all().order_by("name")
    campaignsite = Site.objects.get(slug=site_slug)

    # create a campaign
    if request.method == "POST":
        new_campaign = Campaign()
        new_campaign.name = request.POST["campaign"]
        new_campaign.site = campaignsite

        try:
            new_campaign.save()
        except Exception:
            messages.error(
                request, "Something went wrong. Please check your input and try again."
            )
            return render(
                request=request,
                template_name="CTFLog/site.html",
                context={
                    "sites": sites,
                    "campaigns": None,
                    "campaignsite": campaignsite,
                },
            )

        return redirect("create_ctf", campaign_slug=new_campaign.slug)

    # show the site and the corresponding campaigns
    else:
        campaigns = Campaign.objects.filter(site=campaignsite)
        return render(
            request=request,
            template_name="CTFLog/site.html",
            context={
                "sites": sites,
                "campaigns": campaigns,
                "campaignsite": campaignsite,
            },
        )


@require_http_methods(["GET", "POST"])
@login_required
def create_site(request):
    sites = Site.objects.all().order_by("name")

    if request.method == "POST":
        new_site = Site()
        new_site.name = request.POST["site"]
        new_site.url = request.POST["url"]

        try:
            new_site.save()
        except Exception:
            messages.error(
                request, "Something went wrong. Please check your input and try again."
            )
            return render(
                request=request,
                template_name="CTFLog/create_site.html",
                context={
                    "sites": sites,
                },
            )
        sites.all()  # update queryset to include new page

        return redirect("show_site", site_slug=new_site.slug)

    else:
        sites = Site.objects.all().order_by("name")
        return render(
            request=request,
            template_name="CTFLog/create_site.html",
            context={
                "sites": sites,
            },
        )


@require_http_methods(["GET", "POST"])
@login_required
def show_campaign(request, campaign_slug):
    if request.method == "POST":
        pass
    else:
        sites = Site.objects.all().order_by("name")
        ctf_campaign = Campaign.objects.get(slug=campaign_slug)
        ctfs = CTF.objects.filter(campaign=ctf_campaign, creator=request.user)
        return render(
            request=request,
            template_name="CTFLog/campaign.html",
            context={
                "sites": sites,
                "ctf_campaign": ctf_campaign,
                "ctfs": ctfs,
            },
        )


@require_http_methods(["GET", "POST"])
@login_required
def show_ctf(request, ctf_slug):
    # Fetch data for sidebar and template
    sites = Site.objects.all().order_by("name")
    try:
        ctf = CTF.objects.get(slug=ctf_slug)
    except CTF.DoesNotExist:
        raise Http404("CTF does not exist")
    campaign_ctfs = CTF.objects.filter(campaign=ctf.campaign)

    if request.method == "POST":
        ctf.commands = request.POST["commands"]
        ctf.notes = request.POST["notes"]
        ctf.password = request.POST["password"]
        ctf.public = True if "public" in request.POST else False
        ctf.creator = request.user
        ctf.save()

        messages.info(request, f"You have succesfully updated {ctf.name}")

    return render(
        request=request,
        template_name="CTFLog/ctf.html",
        context={
            "sites": sites,
            "ctf": ctf,
            "campaign_ctfs": campaign_ctfs,
        },
    )


@require_http_methods(["GET", "POST"])
@login_required
def create_ctf(request, campaign_slug, ctf_int=0):
    # Fetch data for sidebar and template
    sites = Site.objects.all().order_by("name")
    try:
        campaign = Campaign.objects.get(slug=campaign_slug)
    except CTF.DoesNotExist:
        raise Http404("Campaign does not exist")

    if request.method == "POST":
        # create ctf

        try:
            ctf = CTF()

            ctf.campaign = campaign
            ctf.name = request.POST["name"]
            ctf.commands = request.POST["commands"]
            ctf.notes = request.POST["notes"]
            ctf.password = request.POST["password"]
            ctf.public = True if "public" in request.POST else False
            ctf.creator = request.user
            ctf.save()

            campaign_ctfs = CTF.objects.filter(campaign=campaign)

            messages.info(request, f"You have succesfully created {ctf.name}")

            return render(
                request=request,
                template_name="CTFLog/ctf.html",
                context={
                    "sites": sites,
                    "ctf": ctf,
                    "campaign_ctfs": campaign_ctfs,
                },
            )
        except IntegrityError as e:
            messages.error(request, f"{e.message}.")
            
            return render(
                request=request,
                template_name="CTFLog/ctf.html",
                context={
                    "sites": sites,
                    "ctf": ctf,
                    "campaign_ctfs": campaign_ctfs,
                },
            )
            

    else:
        if ctf_int:
            ctf_int += 1

        return render(
            request=request,
            template_name="CTFLog/create_ctf.html",
            context={
                "sites": sites,
                "campaign": campaign,
                "ctf_int": ctf_int,
            },
        )
