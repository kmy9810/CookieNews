from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from posting.models import PostingModel

def home(request):
    # all_posting = PostingModel.objects.all()[:11]
    # all_posting.reverse()
    # {'posting': all_posting}
    return render(request, 'home.html')

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
        
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password)
                return redirect('/sign-in')
            

def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user: 
            return redirect('/')
        else:
            return render(request, 'user/signin.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')


@login_required 
def log_out_view(request):
    auth.logout(request)
    return redirect('/')