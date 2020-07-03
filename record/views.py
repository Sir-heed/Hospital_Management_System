from collections import Counter
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import patient_required, staff_required
from users.models import Patient
from .forms import MedicalHistoryForm
from .models import MedicalHistory

def getDataArray(data_dict, field, col1_header, col2_header):
    """It takes a dictionary of objects values, and return the array required by the graph chart"""
    # table.objects.values(field) returns a dict so convert it to list
    rows = [elem[field] for elem in data_dict]
    # Flatten the list while also converting items to lower and strip while space to make the data regular
    rows_list = [elem.lower().strip() for elem in rows]
    # Count items in list
    rows_count = Counter(rows_list)
    # The result array
    result_array = [[col1_header, col2_header]]
    # Append the result with the Counter result
    for i,j in zip(rows_count.keys(), rows_count.values()):
        result_array.append([i.upper(), j])
    # Dump the data for handling in js
    result = json.dumps(result_array)
    return result

"""The home view, it's authenticated, and displays graph using Google Chart API"""
@login_required(login_url='users:login')
def home_view(request):
    # Diseases Chart 
    # Get all entries for the field, note that entries are list of strings
    diseases = [elem['diseases'] for elem in MedicalHistory.objects.values('diseases')]
    disease_list = [item.lower().strip() for elem in diseases for item in elem]
    disease_count = Counter(disease_list)
    data_array = [['Diseases','Number of Patients']]
    for i,j in zip(disease_count.keys(), disease_count.values()):
        data_array.append([i.capitalize(),j])
    disease_data = json.dumps(data_array)

    # Genotype Chart
    # Get all entries for the field, note that enties are strings
    genotypes = MedicalHistory.objects.values('genotype')
    genotype_data = getDataArray(genotypes, 'genotype', 'Genotypes', 'Number of Patients')

    # BloodType Chart
    # Get all entries for the field, note that enties are strings
    bloodgroups = MedicalHistory.objects.values('bloodgroup')
    bloodgroup_data = getDataArray(bloodgroups, 'bloodgroup', 'Blood Groups', 'Number of Patients')

    context = {'disease_data':disease_data, 'genotype_data':genotype_data, 'bloodgroup_data':bloodgroup_data}
    return render(request, 'record/home.html', context)

"""A view to return a table of user details, it can only be viewed by user registered as staff"""
@login_required(login_url='users:login')
@staff_required
def users_details(request):
    # For the search input
    if request.method == 'POST':
        option  = request.POST['disease_options']
        if option == "":
            patients = Patient.objects.all()
        else:
            records_with_disease = MedicalHistory.objects.filter(diseases__contains=[option])
            patients = [record.patient for record in records_with_disease]
    else:
        # Reeturn all patients
        patients = Patient.objects.all()
    # Get all entries for the field, note that entries are list of strings
    diseases = [elem['diseases'] for elem in MedicalHistory.objects.values('diseases')]
    # disease_list = [item.lower().strip() for elem in diseases for item in elem]
    disease_list = [item for elem in diseases for item in elem]
    return render(request, 'record/user_details.html', {'patients':patients,'disease_list':set(disease_list)})

"""A view to allow user to add medical record, this view can only be accessed by user and only once, for update this 
will require the django superuser"""
@login_required(login_url='users:login')
@patient_required
def add_record_view(request):
    # print(request.user)
    try:
        # Check if user has medical history
        mh = request.user.patient.medicalhistory
        context = 'You already have a medical history. Meet the admin if you wish to update your medical history.'
        return render(request, 'record/error.html', {'context':context})
    except MedicalHistory.DoesNotExist:
        if request.method == 'POST':
            # User doesn't have medical history
            form = MedicalHistoryForm(request.POST)
            if form.is_valid():
                record = MedicalHistory(
                    patient = request.user.patient,
                    diseases = form.cleaned_data['diseases'],
                    surgeries = form.cleaned_data['surgeries'],
                    vaccinations = form.cleaned_data['vaccinations'],
                    allergies = form.cleaned_data['allergies'],
                    medications = form.cleaned_data['medications'],
                    bloodgroup = form.cleaned_data['bloodgroup'],
                    genotype = form.cleaned_data['genotype']
                )
                record.save()
                return redirect('record:home')
        else:
            form = MedicalHistoryForm()
        return render(request, 'record/add_record.html', {'form': form})