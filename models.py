from django.db import models
from myadmin.models import *
from datetime import date
from django.contrib.auth.models import User
from django import forms

class Customer_register(models.Model):
	contact = models.BigIntegerField()
	gender  = models.CharField(max_length = 30)
	dob     = models.DateField()
	address = models.TextField()
	state = models.ForeignKey(State_name, on_delete=models.CASCADE)
	city = models.ForeignKey(City_name, on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)
	customer_image = models.CharField(max_length=255,default='')
	user    = models.OneToOneField(User, on_delete = models.CASCADE)
	date = models.DateField(auto_now=True)

	class Meta:
		db_table = 'customer_register'

class Feedback(models.Model):
	rating = models.CharField(max_length=10)
	comment = models.TextField()
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'feedback'

class Contact_us(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=100)
	contact = models.BigIntegerField()
	subject = models.CharField(max_length=30)
	message = models.TextField()
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'contact_us'

class Make_appointment(models.Model):
	physio_clinic = models.ForeignKey(Physio_clinic,on_delete=models.CASCADE)
	appointment_date = models.DateField()
	time = models.CharField(max_length= 30)
	remarks = models.TextField()
	date = models.DateField(default=date.today)
	customer = models.ForeignKey(Customer_register, on_delete=models.CASCADE)
	physio = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=30,default='pending')
	reason = models.TextField()

	class Meta:
		db_table = 'make_appointment'

