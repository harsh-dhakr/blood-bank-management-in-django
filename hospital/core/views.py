
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import PatientRegisterForm, PatientProfileForm ,donarRegisterForm, donarProfileForm
from .forms import BloodDonationForm
from .models import BloodDonation
from .forms import BloodRequestForm
from .models import BloodRequest


def home(request):
   
    return render(request, 'home.html')

def base(request):
   
    return render(request, 'base.html')

def base1(request):
   
    return render(request, 'base1.html')


def patient_register(request):
    if request.method == 'POST':
        user_form = PatientRegisterForm(request.POST)
        profile_form = PatientProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Save Patient Profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # ✅ After register, go to login page
            return redirect('patient_login')

    else:
        user_form = PatientRegisterForm()
        profile_form = PatientProfileForm()

    return render(request, 'patient_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def donar_register(request):
    if request.method == 'POST':
        user_form = donarRegisterForm(request.POST)
        profile_form = donarProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Save donar Profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # ✅ After register, go to login page
            return redirect('donar_login')

    else:
        user_form = donarRegisterForm()
        profile_form = donarProfileForm()

    return render(request, 'donar_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            return render(request, 'patient_login.html', {'error': 'Invalid credentials'})

    return render(request, 'patient_login.html')

def donar_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base1')
        else:
            return render(request, 'donar_login.html', {'error': 'Invalid credentials'})

    return render(request, 'donar_login.html')

def donate_blood(request):
    if request.method == "POST":
        form = BloodDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_history')  # Success page
        else:
            print(form.errors) 
    else:
        form = BloodDonationForm()
    return render(request, 'donar_form.html', {'form': form})

def donation_history(request):
    donations = BloodDonation.objects.all().order_by('-donation_date')
    return render(request, 'donation_history.html', {'donations': donations})



def blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_history')  # Redirect to history page
    else:
        form = BloodRequestForm()
    return render(request, 'blood_request.html', {'form': form})

def request_history(request):
    requests = BloodRequest.objects.all().order_by('-request_date')
    return render(request, 'request_history.html', {'requests': requests})
