from django.db import models

# Create your models here.


class Feature2(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    key = models.CharField(max_length=255, null=False, blank=False)
    data_mode = models.CharField(max_length=255, default="A")
    status = models.BooleanField(default=False)


class Guitar(models.Model):
    guitar_model = models.CharField(max_length=255, null=False, blank=False)
    guitar_type = models.CharField(max_length=255, null=False, blank=False)
    manufacturer = models.CharField(max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    price = models.FloatField(default="0.0", null=False, blank=False)
