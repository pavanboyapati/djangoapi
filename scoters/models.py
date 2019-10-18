from django.db import models


class Scoters(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    is_reserved = models.BooleanField(default=False)
