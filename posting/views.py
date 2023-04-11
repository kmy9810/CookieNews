from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    user = request.user.is_authenticated # 로그인 여부
    redirect('/login')
    # if user:
    #     return redirect('/save_posting')
    # else:
    #     return redirect('/login')

def save_posting(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:

            return render(request, '../templates/posting/save_posting.html')
        else:
            return redirect('/login')