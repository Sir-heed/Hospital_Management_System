from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from .models import MedicalHistory

class MedicalHistoryForm(forms.ModelForm):
    diseases = SimpleArrayField(forms.CharField())
    surgeries = SimpleArrayField(forms.CharField())
    vaccinations = SimpleArrayField(forms.CharField())
    allergies = SimpleArrayField(forms.CharField())
    medications = SimpleArrayField(forms.CharField())

    class Meta:
        model = MedicalHistory
        fields = ('bloodgroup','genotype')
        widgets = {
            'bloodgroup': forms.Select(attrs={
                    # 'class': 'form-control filter-input',
                    'placeholder': 'Blood Group',
                    'required': True}),
                'genotype': forms.Select(attrs={
                    # 'class': 'form-control filter-input',
                    'placeholder': 'Genotype',
                    'required': True}),
        }