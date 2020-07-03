from django.db import models
from django.contrib.postgres.fields import ArrayField
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
    diseases = ArrayField(models.CharField(max_length=100),blank=True)
    surgeries = ArrayField(models.CharField(max_length=100), blank=True)
    vaccinations = ArrayField(models.CharField(max_length=100), blank=True)
    allergies = ArrayField(models.CharField(max_length=100), blank=True)
    medications = ArrayField(models.CharField(max_length=100), blank=True)
    bloodgroup = models.CharField(max_length=2, choices=BLOODGROUP)
    genotype = models.CharField(max_length=2, choices=GENOTYPE)

    def __str__(self):              # __unicode__ on Python 2
        return "{} {}".format(self.patient.user.lastName, self.patient.user.firstName)