from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Patient(User):
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    doctors = models.ManyToManyField('Doctor', blank=True)

class Doctor(User):
    patients = models.ManyToManyField(Patient, blank=True)