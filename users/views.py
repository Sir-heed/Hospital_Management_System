from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import HospitalStaffForm, UserCreationForm, PatientForm

# Create your views here.

# Staff signup view using the User Model Form and HospitalStaff Model Form
def staff_signup_view(request):
    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        staffForm = HospitalStaffForm(request.POST)
        if userForm.is_valid() and staffForm.is_valid():
            user = userForm.save(commit=False)
            user.staff = True
            user.save()
            staff = staffForm.save(commit=False)
            staff.user = user
            staff.save()
            login(request, user)
            return redirect('record:home')
    else:
        userForm = UserCreationForm
        staffForm = HospitalStaffForm
    return render(request, 'users/staff_signup.html', {'userForm': userForm, 'staffForm': staffForm})

# Staff signup view using the User Model Form and Patient Model Form
def patient_signup_view(request):
    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        patientForm = PatientForm(request.POST)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.save()
            login(request, user)
            return redirect('record:home')
    else:
        userForm = UserCreationForm
        patientForm = PatientForm
    return render(request, 'users/patient_signup.html', {'userForm': userForm, 'patientForm': patientForm})

# Login user and redirect user to Home page or the previous page(if a previous page exist)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('record:home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

# Logout user
def logout_view(request):
    logout(request)
    return redirect('users:login')