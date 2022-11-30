from django.contrib import admin
from .models import Site, Campaign, CTF, Favorite


class CampaignInline(admin.TabularInline):
    model = Campaign


class SiteAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    inlines = [
        CampaignInline,
    ]


class CTFInline(admin.TabularInline):
    model = CTF


class CampaignAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    inlines = [
        CTFInline,
    ]


class CTFAdmin(admin.ModelAdmin):
    exclude = ("slug",)


admin.site.register(Site, SiteAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(CTF, CTFAdmin)
admin.site.register(Favorite)
