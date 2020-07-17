from django.db import models
from users.models import Patient

class MedicalHistory(models.Model):
    BLOODGROUP = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    )
    GENOTYPE = (
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS')
    )
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    bloodgroup = models.CharField(max_length=2, choices=BLOODGROUP)
    genotype = models.CharField(max_length=2, choices=GENOTYPE)

    def __str__(self):              # __unicode__ on Python 2
        return "{} {}".format(self.patient.user.lastName, self.patient.user.firstName)

class Disease(models.Model):
    disease_name = models.CharField(max_length=200)
    medicalHistory = models.ManyToManyField(MedicalHistory)

    def __str__(self):
        return self.disease_name

class Surgery(models.Model):
    surgery_name = models.CharField(max_length=200)
    medicalHistory = models.ManyToManyField(MedicalHistory)

    def __str__(self):
        return self.surgery_name

class Vaccination(models.Model):
    vaccination_name = models.CharField(max_length=200)
    medicalHistory = models.ManyToManyField(MedicalHistory)

    def __str__(self):
        return self.vaccination_name

class Allergy(models.Model):
    allergy_name = models.CharField(max_length=200)
    medicalHistory = models.ManyToManyField(MedicalHistory)

    def __str__(self):
        return self.allergy_name

class Medication(models.Model):
    medication_name = models.CharField(max_length=200)
    medicalHistory = models.ManyToManyField(MedicalHistory)

    def __str__(self):
        return self.medication_name