from django.db import models
from .ctf import Site
from django.contrib.auth import get_user_model

class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="favorites", on_delete=models.CASCADE)
    site = models.ForeignKey(Site, related_name="favorites", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.site}"
