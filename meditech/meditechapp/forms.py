from django.forms import ModelForm
from .models import BloodDonation


class BloodDonationForm(ModelForm):
    class Meta:
        model = BloodDonation
        fields = '__all__'
