from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


# class DonnerViewset(viewsets.ModelViewSet):
#     queryset = models.Donner.objects.all()
#     serializer_class = serializers.DonnerSerializer

    
class UserRegistratioApiView(APIView):
    serializer_class = serializers.RegistrationSerializer


    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            return Response("done")
            
        return Response(serializer.errors)