from django import forms
from .models import MedicalHistory, Disease, Surgery, Vaccination, Allergy, Medication

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ('bloodgroup','genotype')
        widgets = {
            'bloodgroup': forms.Select(attrs={
                    'placeholder': 'Blood Group',
                    'required': True}),
                'genotype': forms.Select(attrs={
                    'placeholder': 'Genotype',
                    'required': True}),
        }

class DiseaseForm(forms.ModelForm):
    disease_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
                'placeholder': 'Have you had any disease before, if yes, enter the disease name',
            }))
    class Meta:
        model = Disease
        exclude = ('medicalHistory',)

class SurgeryForm(forms.ModelForm):
    surgery_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
                'placeholder': 'Have you had any surgery before, if yes, enter the surgery name'
            }))
    class Meta:
        model = Surgery
        exclude = ('medicalHistory',)

class VaccinationForm(forms.ModelForm):
    vaccination_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
                'placeholder': 'Have you had any vaccination before, if yes, enter the vaccination name',
            }))
    class Meta:
        model = Vaccination
        exclude = ('medicalHistory',)

class AllergyForm(forms.ModelForm):
    allergy_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
                'placeholder': 'Do you have an allergy, if yes, enter the allergy name'
            }))
    class Meta:
        model = Allergy
        exclude = ('medicalHistory',)

class MedicationForm(forms.ModelForm):
    medication_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
                'placeholder': 'Are you under any medication, if yes, enter the name'
            }))
    class Meta:
        model = Medication
        exclude = ('medicalHistory',)