from django.shortcuts import render, HttpResponse, redirect
import requests
from .forms import *
from django.contrib import messages
from .models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

def schemeEligibility(request):
    return render(request, 'schemeEligibility.html')

def bedsAvailabilty(request):
    response = requests.get('https://api.rootnet.in/covid19-in/hospitals/beds')
    data = response.json()
    regionWise = data["data"]["regional"]
    content = {"regionWise":regionWise}
    return render(request, 'bedsAvailability.html', content)

def testingLab(request):
    from .testingLabApiList import testingApi
    return render(request, 'testingLab.html', {'testingApi':testingApi})

def privateTestingLab(request):
    from .testingLabApiList import testingApi
    return render(request, 'privateTestingLab.html', {'testingApi':testingApi})


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


def guidelines(request):
    return render(request,'guidelines.html',{
        'dead_body_management':'https://www.mohfw.gov.in/pdf/1584423700568_COVID19GuidelinesonDeadbodymanagement.pdf',
        'funeral_guidelines':'https://www.cdc.gov/coronavirus/2019-ncov/daily-life-coping/funeral-guidance.html',
        'islamic_burial':'https://blogs.icrc.org/law-and-policy/2020/04/30/covid-19-islamic-burial-laws/',
        'catholic_burial' : 'https://reliefweb.int/sites/reliefweb.int/files/resources/catholic_covid-19_motd_guidance.pdf',
        'buddhist_burial' : "https://reliefweb.int/sites/reliefweb.int/files/resources/002_buddhist_management_of_the_dead_and_covid-19_web.pdf",
        'funeral':'https://rememberingalife.com/covid-19/planning-a-funeral-during-the-covid-19-pandemic',
        'covid_resources' : 'https://www.instagram.com/rhysjordan_99/guide/covid-19-resources-mumbai/17891399159100687/?igshid=bg2e27jobvaq',
        'guidelines' : 'https://ncdc.gov.in/index1.php?lang=1&level=1&sublinkid=703&lid=550',
        'advice':'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public'
    })

