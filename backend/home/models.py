from django.conf import settings
from django.db import models
class Address(models.Model):
    'Generated Model'
    user = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="address_user",)
    city = models.CharField(max_length=256,)
