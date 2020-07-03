from django.contrib import admin

# Register your models here.
from .models import User, HospitalStaff, Patient
admin.site.register(User)
admin.site.register(HospitalStaff)
admin.site.register(Patient)