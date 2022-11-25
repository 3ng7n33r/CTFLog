from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    site = models.ForeignKey(Site, related_name="campaigns", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CTF(models.Model):
    campaign = models.ForeignKey(
        Campaign, related_name="ctfs", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    commands = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=300, blank=True, null=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name
