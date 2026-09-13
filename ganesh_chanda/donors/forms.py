from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['full_name', 'phone_number', 'amount', 'screenshot']
