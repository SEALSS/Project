from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User


class user(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(primary_key=True, max_length=70)
    number = models.IntegerField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.email


class company_details(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=70)
    id = models.CharField(max_length=100, primary_key=True)
    business_entity = models.CharField(max_length=20)
    company_address = models.CharField(max_length=500)
    pincode = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    keycontact = models.CharField(max_length=70)
    website = models.CharField(max_length=70)
    founded_date = models.CharField(max_length=20)
    number_of_employees = models.IntegerField()
    transport_type = models.CharField(max_length=100)
    clients = models.CharField(max_length=100)
    office_time_from = models.CharField(max_length=50)
    office_time_to = models.CharField(max_length=50)
    factory_time_from = models.CharField(max_length=50)
    factory_time_to = models.CharField(max_length=50)
    core_operation = models.CharField(max_length=200)
    certifications = models.CharField(max_length=100)
    awards = models.CharField(max_length=100)
    overall_area = models.CharField(max_length=50)
    built_area = models.CharField(max_length=50)
    shop_area = models.CharField(max_length=50)

    def __str__(self):
        return self.id







