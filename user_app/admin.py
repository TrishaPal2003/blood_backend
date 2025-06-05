from django.contrib import admin

# Register your models here.
from .models import BloodGroup,Donner,DonationHistory

admin.site.register(BloodGroup)
admin.site.register(Donner)
admin.site.register(DonationHistory)