from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router = DefaultRouter()

# router.register('donnors',views.DonnerViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('register/', views.UserRegistratioApiView.as_view(), name='register'),
    
]

