from collections import Counter
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import patient_required, staff_required
from users.models import Patient
from .forms import MedicalHistoryForm, SurgeryForm, DiseaseForm, VaccinationForm, AllergyForm, MedicationForm
from .models import MedicalHistory, Disease, Surgery, Medication, Vaccination, Allergy

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
    disease_list = Disease.objects.all()
    diseases = [disease.disease_name for disease in disease_list]
    victim = [MedicalHistory.objects.filter(disease=disease).count() for disease in disease_list]
    data_array = [['Diseases','Number of Patients']]
    for i,j in zip(diseases, victim):
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
    print(bloodgroup_data)

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
            disease = Disease.objects.get(disease_name=option)
            records_with_disease = MedicalHistory.objects.filter(disease=disease)
            patients = [record.patient for record in records_with_disease]
    else:
        # Reeturn all patients
        patients = Patient.objects.all()
    diseases = Disease.objects.all()
    context = {'patients':patients,'diseases':diseases}
    return render(request, 'record/user_details.html', context)

"""A view to allow user to add medical record, this view can only be accessed by user and only once, for update this 
will require the django superuser"""
@login_required(login_url='users:login')
@patient_required
def add_record_view(request):
    try:
        # Check if user has medical history
        mh = request.user.patient.medicalhistory
        context = 'You already have a medical history. Meet the admin if you wish to update your medical history.'
        return render(request, 'record/error.html', {'context':context})
    except MedicalHistory.DoesNotExist:
        if request.method == 'POST':
            # User doesn't have medical history hence create a new one
            med_hist_form = MedicalHistoryForm(request.POST)
            surgery_form = SurgeryForm(request.POST)
            allergy_form = AllergyForm(request.POST)
            disease_form = DiseaseForm(request.POST)
            vaccination_form = VaccinationForm(request.POST)
            medication_form = MedicationForm(request.POST)
            form = all([
                med_hist_form.is_valid(),
                surgery_form.is_valid(),
                allergy_form.is_valid(),
                disease_form.is_valid(),
                vaccination_form.is_valid(),
                medication_form.is_valid()
                ])
            if form:
                patient = request.user.patient
                bloodgroup = request.POST.get('bloodgroup')
                genotype = request.POST.get('genotype')
                diseases = request.POST.getlist('disease_name')
                surgeries = request.POST.getlist('surgery_name')
                allergies = request.POST.getlist('allergy_name')
                vaccinations = request.POST.getlist('vaccination_name')
                medications = request.POST.getlist('medication_name')

                # Save medical history
                med_hist = MedicalHistory(patient=patient, bloodgroup=bloodgroup, genotype=genotype)
                med_hist.save()

                # Save disease
                diseases = [disease.strip().lower() for disease in diseases]
                diseases = [disease for disease in diseases if len(disease) > 0]
                for disease in diseases:
                    try:
                        obj = Disease.objects.get(disease_name=disease)
                        obj.medicalHistory.add(med_hist)
                    except Disease.DoesNotExist:
                        disease_obj = Disease(disease_name=disease)
                        disease_obj.save()
                        disease_obj.medicalHistory.add(med_hist)

                # Save surgery
                surgeries = [surgery.strip().lower() for surgery in surgeries]
                surgeries = [surgery for surgery in surgeries if len(surgery) > 0]
                for surgery in surgeries:
                    try:
                        obj = Surgery.objects.get(surgery_name=surgery)
                        obj.medicalHistory.add(med_hist)
                    except Surgery.DoesNotExist:
                        surgery_obj = Surgery(surgery_name=surgery)
                        surgery_obj.save()
                        surgery_obj.medicalHistory.add(med_hist)

                # Save allergy
                allergies = [allergy.strip().lower() for allergy in allergies]
                allergies = [allergy for allergy in allergies if len(allergy) > 0]
                for allergy in allergies:
                    try:
                        obj = Allergy.objects.get(allergy_name=allergy)
                        obj.medicalHistory.add(med_hist)
                    except Allergy.DoesNotExist:
                        allergy_obj = Allergy(allergy_name=allergy)
                        allergy_obj.save()
                        allergy_obj.medicalHistory.add(med_hist)

                # Save vaccination
                vaccinations = [vaccination.strip().lower() for vaccination in vaccinations]
                vaccinations = [vaccination for vaccination in vaccinations if len(vaccination) > 0]
                for vaccination in vaccinations:
                    try:
                        obj = Vaccination.objects.get(vaccination_name=vaccination)
                        obj.medicalHistory.add(med_hist)
                    except Vaccination.DoesNotExist:
                        vaccination_obj = Vaccination(vaccination_name=vaccination)
                        vaccination_obj.save()
                        vaccination_obj.medicalHistory.add(med_hist)

                # Save medication
                medications = [medication.strip().lower() for medication in medications]
                medications = [medication for medication in medications if len(medication) > 0]
                for medication in medications:
                    try:
                        obj = Medication.objects.get(medication_name=medication)
                        obj.medicalHistory.add(med_hist)
                    except Medication.DoesNotExist:
                        medication_obj = Medication(medication_name=medication)
                        medication_obj.save()
                        medication_obj.medicalHistory.add(med_hist)
                return redirect('record:home')
        else:
            med_hist_form = MedicalHistoryForm()
            surgery_form = SurgeryForm()
            allergy_form = AllergyForm()
            disease_form = DiseaseForm()
            vaccination_form = VaccinationForm()
            medication_form = MedicationForm()
        context = {
            'med_hist_form': med_hist_form,
            'surgery_form': surgery_form,
            'allergy_form': allergy_form,
            'disease_form': disease_form,
            'vaccination_form': vaccination_form,
            'medication_form': medication_form
        }
        return render(request, 'record/add_record.html', context)