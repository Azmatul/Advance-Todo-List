from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth import get_user_model
User = get_user_model()

from TodoList.views import *

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login_page.html')

def registration_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('registration_page')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('registration_page')

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login_page')
    return render(request, "registration_page.html")

def logout_view(request):
    logout(request)
    return redirect('login_page')