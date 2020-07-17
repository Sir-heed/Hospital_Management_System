from django.contrib import admin
from .models import MedicalHistory, Disease, Surgery, Medication, Vaccination, Allergy
# Register your models here.
admin.site.register(MedicalHistory)
admin.site.register(Disease)
admin.site.register(Surgery)
admin.site.register(Medication)
admin.site.register(Vaccination)
admin.site.register(Allergy)