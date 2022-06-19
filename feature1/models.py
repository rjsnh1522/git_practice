from django.db import models

# Create your models here.


class Feature1a(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    key = models.CharField(max_length=255, null=False, blank=False)
    data_mode = models.CharField(max_length=255, null=False, blank=False, default="A")
    status = models.BooleanField(default=True)
