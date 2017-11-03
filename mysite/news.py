from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def register(request):
	if request.method == 'POST':
		name = request.POST['name-register']
		college = request.POST['college-register']
		department = request.POST['dept-register']
		year = request.POST['year-register']
		department = request.POST['dept-register']
		telephone = request.POST['tel-register']
		email = request.POST['email-register']
		username = request.POST['username-register']
		password = request.POST['password-register']
		user = User.objects.create (
			first_name = name,
			username = email
			)
		user.set_password(password)
		user.save()
		return redirect('/login/')
	else:	
		return render(request,'customer-register-new.html')	

def login_blog(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = username,password = password)
		if user:	
			login(request,user)
			return  redirect('/posts/')
		else:
			return  HttpResponse('invalid login details')	
	else:	
		return render(request,'login.html')		

def logout_blog(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('/login/')
	else:
		return HttpResponse('you need to log in to log out')	


