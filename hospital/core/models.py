from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class BloodDonation(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.blood_group}"

class BloodRequest(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ])
    units_required = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.blood_group}"