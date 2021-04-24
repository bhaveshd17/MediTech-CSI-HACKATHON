from django.shortcuts import render, HttpResponse, redirect
import requests
from .forms import *
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def bedsAvailabilty(request):
    response = requests.get('https://api.rootnet.in/covid19-in/hospitals/beds')
    data = response.json()
    regionWise = data["data"]["regional"]
    content = {"regionWise":regionWise}
    return render(request, 'bedsAvailability.html', content)

def bloodDonation(request):
    bloodGrp = ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
    if request.method == 'POST':
        bloodDonationForm = BloodDonationForm(request.POST)
        if request.POST.get("bloodGrp") in bloodGrp:
            if request.POST.get("disease") == 'False':
                print("hello")
                if bloodDonationForm.is_valid():
                    bloodDonationForm.save()
                    messages.success(request, "successfully added information!")
                    return redirect('/bloodDonation')
            else:
                messages.warning(request, "Sorry you can't donate blood")
        else:
            messages.warning(request, f"Enter Correct Blood Group")
    content = {}
    return render(request, 'bloodDonation.html', content)

def requestDonation(request):

    if request.method == 'POST':
        bloodGrp = request.POST.get("bloodGrp")
        bloodDonarObj = BloodDonation.objects.filter(bloodGrp=bloodGrp)
        blood_list = []
        for bloodGroup in bloodDonarObj:
            blood_list.append(bloodGroup.bloodGrp)

        content = {'bloodDonarObj':bloodDonarObj, 'bloodGrp':bloodGrp, 'blood_list':blood_list}
    else:
        content = {}
    return render(request, 'requestDonation.html', content)