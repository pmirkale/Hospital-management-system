from django import forms

from . models import *  

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Registration(UserCreationForm):
    class Meta:
            
        model = User
        fields = "username","password1","password2"
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

class ReasonForm(forms.ModelForm):
    class Meta:
        model = Reason
        fields = "__all__"

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = "__all__"

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = "__all__"

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"