from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from user_app.constant import BLOOD_GROUP_CHOICE

class BloodRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICE)
    location = models.CharField(max_length=225)
    message = models.TextField()
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