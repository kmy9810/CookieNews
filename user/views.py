from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
# from posting.models import PostingModel
def home(request):
    # all_posting = PostingModel.objects.all()[:11]
    # all_posting.reverse()
    # {'posting': all_posting}
    return render(request, 'home.html')

def sign_up_view(request):
    return render(request, 'user/signup.html')

def sign_in_view(request):
    return render(request, 'user/signin.html')