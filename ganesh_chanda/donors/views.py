from django.shortcuts import render, redirect
from .forms import DonorForm
from .models import Donor

def home(request):
    return render(request, "donors/home.html")

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, "donors/donor_list.html", {"donors": donors})

def donor_create(request):
    if request.method == "POST":
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "thank_you.html")
    else:
        form = DonorForm()
    return render(request, "donor_form.html", {"form": form})
