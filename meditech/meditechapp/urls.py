from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('bedsAvailability/', views.bedsAvailabilty, name="bedsAvailability"),
	path('bloodDonation/', views.bloodDonation, name="bloodDonation"),
	path('requestDonation/', views.requestDonation, name="requestDonation"),
	path('schemeEligibility/', views.schemeEligibility, name="schemeEligibility"),
	path('guidelines/', views.guidelines, name="guidelines"),
	path('testingLab/', views.testingLab, name="testingLab"),
	path('privateTestingLab/', views.privateTestingLab, name="privateTestingLab"),
]