from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from .models import Login,bloodbankregister,hospitalregister as  reg,donorregister as don
from .models import hospital as hospitalrequest,donor as donorresponse

class Login(CreateView):
    model = Login
    fields = ['User','LoginName','password']
    

def register(request):

  template=loader.get_template('blooddonor/register.html')
  context= {
        'register' : register,
          }
  return HttpResponse(template.render(context, request))	



class bloodbankregister(CreateView):
	model=bloodbankregister
	fields=['BloodBankName','BloodBankAddress','BloodBankMobileNumber','BloodBankEmailId','password']

class hospitalregister(CreateView):
	model=reg
	fields=['HospitalName','HospitalAddress','HospitalMobileNumber','HospitalEmailId','password']

class donorregister(CreateView):
	model=don
	fields=['DonorName','DonorAddress','DonorMobileNumber','DonorAge','DonorEmailId','password']

def bloodbank(request,LoginName,User):

   if User == 'bloodbank':
    request.session['LoginName']= LoginName
    request.session['User']= User
    template=loader.get_template('blooddonor/bloodbank.html')
    context= {
        
      'LoginName' :request.session['LoginName'],
      'User' : request.session['User']
      }
    return HttpResponse(template.render(context, request))
   

   



class hospital(CreateView):
	model=hospitalrequest
	fields=['BloodGroup','TypeOfBlood','NumberOfUnits','Date','Time']

class donor(CreateView):
	model=donorresponse
	fields=['BloodGroup','TypeOfBlood','Date','Time','NearByBloodBank']
def viewhospital(request):
  hos=reg.objects.all()
  hospital=hospitalrequest.objects.all()
  template=loader.get_template('blooddonor/viewhospital.html')
  context= {
         'hos':hos,
         'hospital':hospital,
           
        # 'order':order, 
         
     #'json_list':json_list,
        #'EmailId' :request.session['EmailId'],
        #'User' : request.session['User']
          }
  return HttpResponse(template.render(context, request))

  
def viewdonor(request):
  hos=don.objects.all()
  hospital=donorresponse.objects.all()
  template=loader.get_template('blooddonor/viewdonor.html')
  context= {
        
      'hospital':hospital,
      'hos':hos
           
        # 'order':order, 
         
     #'json_list':json_list,
        #'EmailId' :request.session['EmailId'],
        #'User' : request.session['User']
          }
  return HttpResponse(template.render(context, request))
