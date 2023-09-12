from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import *

# Create your views here.
def home(request):
  return render(request, 'home.html')

def register_page(request):
  return render(request, 'register.html')

def register(request):
  if request.method == 'POST':
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    user_name = request.POST['uname']
    email_id = request.POST['email']
    mobile = request.POST['phone']
    passw = request.POST['password']
    c_passw = request.POST['cpassword']
    
    if passw == c_passw:
      if User.objects.filter(username = user_name).exists():
        # messages.info(request, 'Sorry, Username already exists')
        # return redirect('register')
        return redirect('log')
      elif Customer.objects.filter(cust_mobile = mobile).exists():
        # messages.info(request, 'Sorry, Mobile Number already exists')
        # return redirect('register')
        return redirect('log')

      elif not User.objects.filter(email = email_id).exists():
    
        user_data = User.objects.create_user(first_name = first_name,
                        last_name = last_name,
                        username = user_name,
                        email = email_id,
                        password = passw)
        user_data.save()
        
        data = User.objects.get(id = user_data.id)
        cust_data = Customer(cust_mobile = mobile,
                             cust_user = data)
        cust_data.save()
        return redirect('log')
      else:
        # messages.info(request, 'Sorry, Email already exists')
        # return redirect('register')
        return redirect('log')
      
      
def login(request):
  if request.method == 'POST':
    user_name = request.POST['username']
    passw = request.POST['password']
    
    log_user = auth.authenticate(username = user_name,
                                  password = passw)
    
    if log_user is not None:
      auth.login(request, log_user)
      return redirect('homepage')
    else: 
      return redirect('log')
    
def homepage(request):
  return render(request, 'homepage.html')

    
    
    