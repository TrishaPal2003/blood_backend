# signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Donner


def create_donner_profile(sender, instance, created, **kwargs):
    if created:
        Donner.objects.create(user=instance)


post_save.connect(create_donner_profile, sender=User)
