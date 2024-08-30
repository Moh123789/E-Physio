from django.db import models
from myadmin.models import *
from datetime import date
from django.contrib.auth.models import User
from django import forms

class Physio_registration(models.Model):
	address = models.TextField()
	contact = models.BigIntegerField()
	gender = models.CharField(max_length=10)
	dob = models.DateField()
	experience = models.CharField(max_length=20)
	degree = models.CharField(max_length=20)
	degree_reg_no = models.CharField(max_length=20)
	state = models.ForeignKey(State_name, on_delete=models.CASCADE)
	city = models.ForeignKey(City_name, on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)
	physio_image = models.CharField(max_length=255)
	physio = models.OneToOneField(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)

	class Meta:
		db_table = 'physio_registration'

class Service(models.Model):
	title = models.CharField(max_length=30)
	description = models.TextField()
	service_image = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	duration = models.CharField(max_length=10)
	physio = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		db_table = 'service'

class Manage_physio(models.Model):
	physio_clinic = models.ForeignKey(Physio_clinic,on_delete=models.CASCADE)
	day = models.CharField(max_length=100)
	fromtime = models.CharField(max_length=30)
	totime = models.CharField(max_length=30)
	fees = models.DecimalField(max_digits=7, decimal_places=2)
	physio = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		db_table = 'manage_physio'
