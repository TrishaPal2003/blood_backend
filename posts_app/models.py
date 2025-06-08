# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from user_app.constant import BLOOD_GROUP_CHOICE


class BloodRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICE)
    location = models.CharField(max_length=225)
    message = models.TextField()
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"


class DonationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICE)
    location = models.CharField(max_length=225)
    donate_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}"
