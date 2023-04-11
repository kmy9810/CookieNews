from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def sign_up_view(request):
    return render(request, 'user/signup.html')

def sign_in_view(request):
    return render(request, 'user/signin.html')