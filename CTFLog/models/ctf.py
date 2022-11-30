from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Site(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_site", kwargs={"site_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    site = models.ForeignKey(Site, related_name="campaigns", on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_campaign", kwargs={"campaign_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.site.name}-{self.name}")
        return super().save(*args, **kwargs)


class CTF(models.Model):
    campaign = models.ForeignKey(
        Campaign, related_name="ctfs", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    commands = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=300, blank=True, null=True)
    public = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_ctf", kwargs={"ctf_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"{self.campaign.site.name}-{self.campaign.name}-{self.name}"
            )
        return super().save(*args, **kwargs)
