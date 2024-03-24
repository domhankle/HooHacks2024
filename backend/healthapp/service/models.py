from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Patient(User):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True, null=True, default=None)
    doctors = models.ManyToManyField('Doctor', blank=True)
    address = models.CharField(max_length=100, blank=True)
    appointments = models.ManyToManyField('Appointment', blank=True)
    prescriptions = models.ManyToManyField('Prescription', blank = True)
    immunizations = models.ManyToManyField('Immunization', blank = True)

class Appointment(models.Model):
    date = models.IntegerField()
    doctor = models.ManyToManyField('Doctor', blank=True)
    complete = models.BooleanField()
    vitals = models.OneToOneField('Vitals', on_delete=models.CASCADE, blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True)
    reason_for_visit = models.CharField(max_length=100, blank=True, null=True, default=None)

class Vitals(models.Model):
    weight = models.CharField(max_length=100, blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)

class Prescription(models.Model):
    name = models.CharField(max_length=100)
    start = models.IntegerField()
    end = models.IntegerField()
    refill = models.BooleanField()

class Immunization(models.Model):
    name = models.CharField(max_length=100)
    up_to_date = models.BooleanField()
    expires = models.IntegerField()

class Doctor(User):
    name = models.CharField(max_length=100, blank=True)
    patients = models.ManyToManyField(Patient, blank=True)
