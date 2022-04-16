from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials!!")
            return redirect('login_user')
    return render(request, "accounts/login.html")

def register_user(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exits!!")
                return redirect("register_user")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email Already exits!!")
                    return redirect("register_user")
                else:
                    user = User(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, "Account register Successfully")
                    return redirect("login_user")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register_user")
    return render(request, "accounts/register.html")

def logout_user(request):
    logout(request)
    return redirect("login_user")

@login_required(login_url="login_user")
def dashboard(request):
    return render(request, "accounts/dashboard.html")