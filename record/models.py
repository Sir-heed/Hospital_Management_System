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
    name = models.CharField(max_length=200)
    medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name="disease")

    def __str__(self):
        return self.name

class Surgery(models.Model):
    name = models.CharField(max_length=200)
    medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name="surgery")

    def __str__(self):
        return self.name

class Vaccination(models.Model):
    name = models.CharField(max_length=200)
    medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name="vaccination")

    def __str__(self):
        return self.name

class Allergy(models.Model):
    name = models.CharField(max_length=200)
    medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name="allergy")

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.CharField(max_length=200)
    medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name="medication")

    def __str__(self):
        return self.name