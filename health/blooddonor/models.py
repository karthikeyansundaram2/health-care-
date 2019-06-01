from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from datetime import date
from datetime import time
from django.utils.translation import gettext as _

ROLE = (
	('bloodbank','BLOODBANK'),
	('hospital','HOSPITAL'),
	('donor','DONOR'),
	)

class Login(models.Model):

	LoginName = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
    
	User = models.CharField(max_length=20, choices=ROLE, default='bloodbank')

	def get_absolute_url(self):

		if self.User == 'bloodbank':
			#request.session['LoginId']='123'
			#return HttpResponse('hello'+request.session['LoginId'])  
			return reverse('bloodbank',kwargs={'LoginName':self.LoginName,'User':self.User})
			#model.addAttribute('LoginId',self.LoginId,'views.py')
		elif self.User == 'hospital':
			return reverse('hospital')
		else:
			return reverse('donor')

class bloodbankregister(models.Model):
	BloodBankName=models.CharField(max_length=45)
	BloodBankAddress=models.CharField(max_length=300)
	BloodBankMobileNumber=models.CharField(max_length=10)
	BloodBankEmailId=models.EmailField(max_length=254)
	password=models.CharField(max_length=15)
	def get_absolute_url(self):
		return reverse('bloodbankregister')

class hospitalregister(models.Model):
	HospitalName=models.CharField(max_length=50)
	HospitalAddress=models.CharField(max_length=300)
	HospitalMobileNumber=models.CharField(max_length=10)
	HospitalEmailId=models.EmailField(max_length=254)
	password=models.CharField(max_length=15)
	def get_absolute_url(self):
		return reverse('hospitalregister')


class donorregister(models.Model):
	DonorName=models.CharField(max_length=50)
	DonorAddress=models.CharField(max_length=300)
	DonorMobileNumber=models.CharField(max_length=10)
	DonorAge=models.CharField(max_length=3)
	DonorEmailId=models.EmailField(max_length=254)
	password=models.CharField(max_length=15)
	def get_absolute_url(self):
		return reverse('donorregister')



class hospital(models.Model):
	BloodGroup=models.CharField(max_length=5)
	TypeOfBlood=models.CharField(max_length=3)
	NumberOfUnits=models.IntegerField()
	Date=models.DateField(_("Date"), default=date.today)
	Time=models.TimeField(blank=True, null=True)
    
	def get_absolute_url(self):
		return reverse('hospital')

class donor(models.Model):
	BloodGroup=models.CharField(max_length=5)
	TypeOfBlood=models.CharField(max_length=3)
	
	Date=models.DateField(_("Date"), default=date.today)
	Time=models.TimeField(blank=True, null=True)
	NearByBloodBank=models.CharField(max_length=30)

	def get_absolute_url(self):
		return reverse('donor')