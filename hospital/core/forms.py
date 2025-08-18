from django import forms
from django.contrib.auth.models import User
from .models import PatientProfile
from .models import BloodDonation
from .models import BloodRequest

class PatientRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['phone', 'address']

class donarRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class donarProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['phone', 'address']


class BloodDonationForm(forms.ModelForm):
    class Meta:
        model = BloodDonation
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'donation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['name', 'age', 'blood_group', 'units_required', 'contact_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'units_required': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Units of blood'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact number'}),
        }