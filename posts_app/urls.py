from django.urls import path
from . import views

urlpatterns = [
    path('wall/', views.BloodRequestView.as_view(), name='blood-wall'),
    path('history/', views.DonationHistoryListCreateView.as_view(), name='donation-history'),
]
