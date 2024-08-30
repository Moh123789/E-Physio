from django.shortcuts import render,redirect
from myadmin.models import *
from customer.models import * 
from physio.models import * 
from django.contrib.auth.models import User
from django.contrib import auth,messages
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def layout(request):
	context = {}
	return render(request,'customer/common/layout.html',context)

def home(request):
	result = City_name.objects.all()
	result1 = Area.objects.all()
	context = {'cities':result,'areas':result1}
	return render(request,'customer/home.html',context)

def about(request):
	context = {}
	return render(request,'customer/about.html',context)

def customer_registration(request):
	result1 = State_name.objects.all()
	result2 = City_name.objects.all()
	result3 = Area.objects.all()
	context = {'state':result1,'city':result2,'area':result3}
	return render(request,'customer/customer_registration.html',context)

def customer_store(request):
	#user
	fname = request.POST['fname']
	lname = request.POST['lname']
	uname = request.POST['uname']
	email = request.POST['email']
	password = request.POST['password']
	cpassword = request.POST['cpassword']

	contact = request.POST['contact']
	address = request.POST['address']
	gender = request.POST['gender']
	dob = request.POST['dob']
	state = request.POST['statename']
	city = request.POST['cityname']
	area = request.POST['areaname']
	
	myfile = request.FILES['uimg']
	mylocation = os.path.join(settings.MEDIA_ROOT, 'customer_upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(myfile.name,myfile)

	if password == cpassword:
		result = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
		Customer_register.objects.create(address=address,contact=contact,gender=gender,dob=dob,state_id=state,city_id=city,area_id=area,customer_image=myfile,user_id=result.id)
		return redirect('/customer/customer_registration')	
	else:
		messages.warning(request,'Missmatch Password')

def customer_edit_profile(request):
	result1 = State_name.objects.all()
	result2 = City_name.objects.all()
	result3 = Area.objects.all()
	id = request.user.id
	result = Customer_register.objects.get(user_id=id)
	# date1 = Customer_register.objects.get(user_id=user_id).date
	# date = date1.strftime("%Y-%m-%d")
	context = {'result':result,'state':result1,'city':result2,'area':result3}
	return render(request, 'customer/customer_edit_profile.html' ,context)

def customer_update(request,id):
	print(len(request.FILES))
	fname = request.POST['fname']
	lname = request.POST['lname']
	uname = request.POST['uname']
	email = request.POST['email']

	contact = request.POST['contact']
	address = request.POST['address']
	gender = request.POST['gender']
	dob = request.POST['dob']
	state = request.POST['statename']
	city = request.POST['cityname']
	area = request.POST['areaname']
	# myfile = request.FILES['pimg']
    
	if len(request.FILES) == 0:
		ci = Customer_register.objects.get(pk=id)
		myfilename = ci.customer_image
	else:
		myfile = request.FILES['uimg']
		mylocation = os.path.join(settings.MEDIA_ROOT, 'customer_upload')
		obj = FileSystemStorage(location=mylocation)
		obj.save(myfile.name,myfile)
		myfilename = myfile.name

	data = {
            'contact' : contact,
            'address' : address,
            'gender' : gender,
            'dob' : dob,
            'state_id': state,
            'city_id' : city,
            'area_id' : area,
            'customer_image' : myfilename
           }
	
	data1 = {
            'first_name' : fname,
            'last_name' : lname,
            'username' : uname,
            'email' : email
            }
	user = User.objects.update_or_create(pk=request.user.id,defaults=data1)
	Customer_register.objects.update_or_create(pk=id,defaults=data)
	return redirect('/customer/home')


def customer_login(request):
	context = {}
	return render(request,'customer/customer_login.html',context)

def login_check(request):
	username = request.POST['username']
	password = request.POST['password']
	
	result = auth.authenticate(username=username,password=password)

	if result is None:
		messages.warning(request,'Invalid Username and Password')
		return redirect('/customer/customer_login')
	else:
		auth.login(request,result)
		return redirect('/customer/home')

def customer_logout(request):
	auth.logout(request)
	return redirect('/customer/customer_login')

def feedback(request):
	context = {}
	return render(request,'customer/feedback.html',context)

def feedback_store(request):
	myrating  = request.POST['rating']
	mycomment = request.POST['comment']
	id = request.user.id

	if Feedback.objects.filter(user_id=id):
		return redirect('/customer/applied_feedback')
	else:
		Feedback.objects.create(rating=myrating, comment = mycomment, user_id=id)
		messages.success(request,'Thank You For Your Valuable Feedback')
		return redirect('/customer/thanks')

def thanks(request):
	context = {}
	return render(request, 'customer/thanks.html', context)

def applied_feedback(request):
	context = {}
	return render(request, 'customer/applied_feedback.html', context)

def contact(request):
	context = {}
	return render(request, 'customer/contact.html', context)

def contact_store(request):
	name    = request.POST['name']
	email   = request.POST['email']
	contact = request.POST['contact']
	subject = request.POST['subject']
	message = request.POST['message']

	Contact_us.objects.create(name=name, email = email,contact=contact,subject=subject,message=message)
	messages.success(request,'Thank You for sharing this with us,we will reply by email as soon as possible')

	return redirect('/customer/contact')

def physios(request):
	result  = Physio_registration.objects.all()
	context = {'physios':result}
	return render(request,'customer/physio.html',context)






def view_physio(request,id):
	result  = Physio_registration.objects.get(physio_id=id)
	result1 = Service.objects.filter(physio_id=id)
	result2 = Manage_physio.objects.filter(physio_id=id)

	context = {'physio':result,'services':result1,'clinic':result2}
	return render(request,'customer/view_physio.html',context)

# @login_required(login_url="/customer/customer_login")
def appointment(request,id):
	result  = Physio_registration.objects.get(physio_id=id)
	result1 = Manage_physio.objects.filter(physio_id=id)

	context = {'clinic':result1,'physio_id':id}
	return render(request,'customer/appointmaint.html',context)

def appointment_store(request):
	clinic = request.POST['clinic']
	appointment_date = request.POST['appoint_date']
	time   = request.POST['time']
	remarks = request.POST['remarks']
	physio = request.POST['physio_id']

	id = request.user.id
	user_p = Customer_register.objects.get(user_id=id)
	uid=user_p.id

	Make_appointment.objects.create(physio_clinic_id=clinic,appointment_date=appointment_date,time=time,remarks=remarks,customer_id=uid,physio_id=physio)
	return redirect('/customer/thankyou')

def thankyou(request):
	# result = Category.objects.all()
	context = {}
	return render(request, 'customer/thankyou.html', context)

def my_appointment(request):
	id      = request.user.id
	user_p  = Customer_register.objects.get(user_id=id)
	uid     =user_p.id
	result  = Make_appointment.objects.filter(customer_id=uid)
	context = {'result':result}
	return render(request,'customer/my_appointment.html',context)

def search_beautician(request):
	city_id = request.POST['city']
	area_id = request.POST['area']

	result  = Physio_registration.objects.filter(city_id=city_id,area_id=area_id)
	context = {'result': result}
	return render(request,'customer/search_beautician.html',context)

def view_physio(request,id):
	result  = Physio_registration.objects.get(physio_id=id)
	result1 = Service.objects.filter(physio_id=id)
	result2 = Manage_physio.objects.filter(physio_id=id)

	context = {'physio':result,'services':result1,'clinic':result2}
	return render(request,'customer/view_physio.html',context)

def changepass(request):
	context = {}
	return render(request, 'customer/changepass.html' ,context)

def changepass_update(request):
	username      = request.user.username
	old_password  = request.POST['old_password']
	new_password  = request.POST['new_password']
	rnew_password = request.POST['rnew_password']

	if new_password == rnew_password:
		user = auth.authenticate(username=username, password=old_password)
		if user is not None:
			user.set_password(new_password)
			user.save()
			messages.success(request, 'Password Updated Successfully')
			return redirect('/customer/customer_login')
		else:
			messages.success(request, 'Invalid Password Try Again')
			return redirect('/customer/changepass')
	else:
			messages.success(request, 'Miss Match Password')




