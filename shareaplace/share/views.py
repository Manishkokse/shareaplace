from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.response import TemplateResponse
from django.core.mail import send_mail
from django.core.signing import Signer
from django.shortcuts import render
from models import SignUp
import re
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
# Create your views here.
def home(request,params=None,id=None):
    #if request.user.is_authenticated():
         #return redirect('dashboard.html')
    return TemplateResponse( request, "index.html", context={})

def signup(request):
    
    email = request.GET.get('email', None)
    firstname = request.GET.get('firstname', None)
    lastname = request.GET.get('lastname', None)
    phone = request.GET.get('phone', None)
    password1 = request.GET.get('password1', None)
    clearPassNoHash = password1.replace(" ", "")
    password = make_password(clearPassNoHash, None, 'md5')
    #print email,firstname,lastname,phone,password1
    
    data = {
        'is_taken': SignUp.objects.filter(email__iexact=email).exists()

        }
    
        
    #print data['is_taken']
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    else:
        obj=SignUp(firstname=firstname,lastname=lastname,email=email,mobile=phone,password=password)
	
        obj.save()
	data = {
        'ok': 'ok'

        }
    return JsonResponse(data)


def login(request):
    email = request.GET.get('email', None)
    password = request.GET.get('password', None)
    clearPassNoHash = password.replace(" ", "")
    password = make_password(clearPassNoHash, None, 'md5')
    user = SignUp.objects.get(email=email, password=password)
    if user is not None:
    # the password verified for the user
        if user.is_active:
           return redirect('dashboard.html')
        else:
            data = {
        'ok': 'ok'

        }
            return JsonResponse(data)
    else:
    # the authentication system was unable to verify the username and password
        data = {
        'error': 'error'

        }
        return JsonResponse(data)




@login_required(login_url='/') #if not logged in redirect to /
def dashboard(request):        
    return TemplateResponse(request, 'dashboard.html')

	
	

def otp(request):
    otp = request.GET.get('otp', None)
    phone = request.GET.get('mobile', None)
    #print otp,phone
    mobile=int(phone)
    print mobile
    try:
		user = SignUp.objects.get(otp=otp,mobile=mobile)
		print user    
		if user is not None:
			if user.is_active:
				return TemplateResponse(request, "dashboard.html", context={})	
			else:
				user.is_active=1
				user.save()
				return TemplateResponse(request, 'dashboard.html')
		

    except Exception ,e:
        # the authentication system was unable to verify the otp and mobile
		data = {
			'error': 'error'

			}
		return JsonResponse(data)








