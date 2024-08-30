from django.shortcuts import render,redirect
from myadmin.models import *
from customer.models import * 
from physio.models import * 
from django.contrib.auth.models import User
from django.contrib import auth,messages
from datetime import datetime, date
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

def layout(request):
	context = {}
	return render(request,'physio/common/layout.html',context)

def home(request):
	context = {}
	return render(request,'physio/home.html',context)

def physio_registration(request):
	result1 = State_name.objects.all()
	result2 = City_name.objects.all()
	result3 = Area.objects.all()
	context = {'state':result1,'city':result2,'area':result3}
	return render(request,'physio/physio_registration.html',context)

def physio_store(request):
	#user
	fname = request.POST['fname']
	lname = request.POST['lname']
	uname = request.POST['uname']
	email = request.POST['email']
	password = request.POST['password']
	cpassword = request.POST['cpassword']


    #profile
	experience = request.POST['experience']
	degree = request.POST['degree']
	degree_reg_no = request.POST['drg']
	contact = request.POST['contact']
	address = request.POST['address']
	gender = request.POST['gender']
	dob = request.POST['dob']
	state = request.POST['statename']
	city = request.POST['cityname']
	area = request.POST['areaname']
	myfile = request.FILES['pimg']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'physio_upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(myfile.name,myfile)

	if password == cpassword:
		result = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
		Physio_registration.objects.create(experience=experience,degree=degree,degree_reg_no=degree_reg_no,address=address,contact=contact,gender=gender,dob=dob,state_id=state,city_id=city,area_id=area,physio_image=myfile,physio_id=result.id)
		return redirect('/physio/home')
	else:
		messages.warning(request,'Missmatch Password')

def edit_physio_details(request):
	print(len(request.FILES))
	result1 = State_name.objects.all()
	result2 = City_name.objects.all()
	result3 = Area.objects.all()
	id = request.user.id
	result = Physio_registration.objects.get(physio_id=id)
	context = {'result':result,'state':result1,'city':result2,'area':result3}
	return render(request,'physio/edit_physio_details.html',context)

def physio_update(request,id):
	fname = request.POST['fname']
	lname = request.POST['lname']
	uname = request.POST['uname']
	email = request.POST['email']

    #profile
	experience = request.POST['experience']
	degree = request.POST['degree']
	degree_reg_no = request.POST['drg']
	contact = request.POST['contact']
	address = request.POST['address']
	gender = request.POST['gender']
	dob = request.POST['dob']
	state = request.POST['statename']
	city = request.POST['cityname']
	area = request.POST['areaname']
	
	

	if len(request.FILES) == 0:
		pimgs = Physio_registration.objects.get(pk=id)
		myfilename = pimgs.physio_image
	else:
		myfile = request.FILES['pimg']
		mylocation = os.path.join(settings.MEDIA_ROOT, 'physio_upload')
		obj = FileSystemStorage(location=mylocation)
		obj.save(myfile.name,myfile)
		myfilename = myfile.name

	
	data = {
            'contact' : contact,
            'address' : address,
            'gender' : gender,
            'dob' : dob,
            'experience' : experience,
            'degree' : degree,
            'degree_reg_no' : degree_reg_no,
            'state_id' : state,
            'city_id' : city,
            'area_id' : area,
            'physio_image' : myfilename
           }
	data1 = {
            'first_name' : fname,
            'last_name' : lname,
            'username' : uname,
            'email' : email
            }
	user = User.objects.update_or_create(pk=request.user.id,defaults=data1)
	Physio_registration.objects.update_or_create(pk=id,defaults=data)
	return redirect('/physio/edit_physio_details')

def services(request):
	context = {}
	return render(request,'physio/services.html',context)

def services_store(request):
	mytitle = request.POST['title']
	mydescription = request.POST['description']

	myfile = request.FILES['simg']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'physio_upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(myfile.name,myfile)

	myprice = request.POST['price']
	myduration = request.POST['duration']
	id = request.user.id
	
	Service.objects.create(title=mytitle,description=mydescription,service_image=myfile,price=myprice,duration=myduration,physio_id=id)
	return redirect('/physio/services')



def all_services(request):
	id = request.user.id
	result = Service.objects.filter(physio_id=id)
	context = {'services':result}
	return render(request,'physio/all_services.html',context)

def delete_services(request,id):
	result = Service.objects.get(pk=id)
	result.delete()
	return redirect('/physio/all_services')

def edit_services(request,id):
	result = Service.objects.get(pk=id)
	context = {'result':result}
	return render(request,'physio/edit_services.html',context)

def update_services(request,id):
	mytitle = request.POST['title']
	mydescription = request.POST['description']

	if len(request.FILES) == 0:
		si = Service.objects.get(pk=id)
		myfilename = si.service_image
	else:
		myfile = request.FILES['simg']
		mylocation = os.path.join(settings.MEDIA_ROOT, 'physio_upload')
		obj = FileSystemStorage(location=mylocation)
		obj.save(myfile.name,myfile)
		myfilename = myfile.name

	myprice = request.POST['price']
	myduration = request.POST['duration']

	data = {
			'title' : mytitle,
			'description' :mydescription,
			'service_image':myfilename,
			'price':myprice,
			'duration' :myduration
	}

	Service.objects.update_or_create(pk=id,defaults=data)
	return redirect('/physio/all_services')

# @login_required(login_url="/physio/physio_login")
def manage_physio(request):
	result = Physio_clinic.objects.all()
	context = {'result':result}
	return render(request,'physio/manage_physio.html',context)

# @login_required(login_url="/physio/physio_login")
def manage_physio_store(request):
	clinic = request.POST['clinic']

	myday_list = request.POST.getlist('day[]')
	myday_str = ','.join(myday_list)
	
	myfromtime = request.POST['from']
	mytotime = request.POST['to']
	myfees = request.POST['fees']
	physio_id = request.user.id

	Manage_physio.objects.create(physio_clinic_id=clinic,day=myday_str,fromtime=myfromtime,totime=mytotime,fees=myfees,physio_id=physio_id)
	return redirect('/physio/manage_physio')



def physio_login(request):
	context = {}
	return render(request,'physio/physio_login.html',context)

def login_check(request):
	username = request.POST['username']
	password = request.POST['password']
	
	result = auth.authenticate(username=username,password=password)

	if result is None:
		messages.warning(request,'Invalid Username and Password')
		return redirect('/physio/physio_login')
	else:
		auth.login(request,result)
		return redirect('/physio/home')

def physio_logout(request):
	auth.logout(request)
	return redirect('/physio/physio_login')

def user_appointment(request):
	id = request.user.id
	result = Make_appointment.objects.filter(physio_id=id, status='pending')
	context = {'appointments':result}
	return render(request,'physio/user_appointment.html',context)

def apply_appointment(request,id):
	result = Make_appointment.objects.get(pk=id)
	context = {'appointment':result}
	return render(request,'physio/apply_appointment.html', context)

def apply_appointment_store(request,id):
	apply_appointment = request.POST['apply']
	reason = request.POST['reason']
	data = {
            'reason' : request.POST['reason'],
            'status' : request.POST['apply'],
        }

	Make_appointment.objects.update_or_create(pk=id,defaults=data)
	return redirect('/physio/user_appointment')

def my_apply_appointment(request):
	id = request.user.id 
	if request.method =='POST':
		s_date = request.POST['date']
		result = Make_appointment.objects.filter(physio_id=id,status='approved',appointment_date = s_date)
	else:
		result = Make_appointment.objects.filter(physio_id=id,status='approved',appointment_date = date.today())

	context = {'result':result}
	return render(request,'physio/my_apply_appointment.html',context)



