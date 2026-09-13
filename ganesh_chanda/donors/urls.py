from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("donate/", views.donor_create, name="donate"),
    path('donors/', views.donor_list, name='donor_list'),
]

