from django.contrib import admin
from django.db import models

class Donor(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    screenshot = models.ImageField(upload_to="screenshots/")
    created_at = models.DateTimeField(auto_now_add=True)

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'amount')
    search_fields = ('full_name', 'phone_number')
    list_filter = ('amount',)

    def __str__(self):
        return f"{self.full_name} - {self.amount}"
