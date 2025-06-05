from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Donner
from .constant import BLOOD_GROUP_CHOICE


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    blood_group = serializers.CharField(choices = BLOOD_GROUP_CHOICE)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'blood_group']

    def validate(self, data):
        if data['password'] != data['confirm_password']