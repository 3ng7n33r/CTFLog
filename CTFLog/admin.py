from django.contrib import admin
from .models import Site, Campaign, CTF

class CampaignInline(admin.TabularInline):
    model = Campaign


class SiteAdmin(admin.ModelAdmin):
    inlines = [
        CampaignInline,
    ]

class CTFInline(admin.TabularInline):
    model = CTF

class CampaignAdmin(admin.ModelAdmin):
    inlines = [
        CTFInline,
    ]    

admin.site.register(Site, SiteAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(CTF)