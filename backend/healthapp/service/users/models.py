from django.db import models

class User(models.Model):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN'
        DOCTOR = 'DOCTOR'
        PATIENT = 'PATIENT'

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=Role.choices)

class Patient(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

class Doctor(models.Model):
    username  = models.CharField(max_length=100)
 #   patients = models.ManyToManyField(Patient, blank=True)

