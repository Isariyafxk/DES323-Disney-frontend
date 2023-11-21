from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from disneyland.models import *
from hello_world import *
import pandas as pd
# Create your views here.

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def home(request):
    context = {}
    return render(request, "webpages/home.html", context=context)

def editprofile(request):
    context = {}
    return render(request, "webpages/editprofile.html", context=context)

def places(request):
    context = {}
    return render(request, "webpages/places.html", context=context)


def register(request):
    if request.method == 'POST':
        username = request.POST['r_username']
        name = request.POST['r_name']
        email = request.POST['r_email']
        password = request.POST['r_password']
        confirmpassword = request.POST['r_cpassword']
         
        if userInfo.objects.filter(userName=username):
            context_data ={
                "message":"Registered username"
            }
            return render(request,"webpages/register.html",context_data)
        if userInfo.objects.filter(email=email):
            context_data ={
                "message":"Registered email"
            }
            return render(request,"webpages/register.html",context_data)
        new_item = userInfo (
                userName = username,
                name = name,
                email = email,
                passWord = password,
                confirmpass = confirmpassword
            )   
        new_item.save()

        alert_message = "Registration successful! You can now log in."
        return render(request, "webpages/login.html", {"alert_message": alert_message})
    return render(request, "webpages/register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('l_email')
        password = request.POST.get('l_password')
        # Check if the user exists with the provided email
        if (email == ''):
            context_data = {
                "message": "Enter the email",
            }
            return render(request, "webpages/login.html", context_data)
        # Log in successful, you can redirect to the home page or any other page
        return redirect('/home')

    return render(request, "webpages/login.html")

def profile(request):
    # Retrieve the latest user data
    latest_user = userInfo.objects.latest()
    # Pass the user data to the template
    context = {
        'user': latest_user,
    }

    return render(request, "webpages/profile.html", context)



    





