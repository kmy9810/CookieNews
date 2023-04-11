# from datetime import datetime
from django.shortcuts import render, redirect
from .models import PostingModel
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     user = request.user.is_authenticated # 로그인 여부
#     redirect('/login')
#     # if user:
#     #     return redirect('/save_posting')
#     # else:
#     #     return redirect('/login')


def save_posting(request):
    if request.method == 'GET':
        # user = request.user.is_authenticated
        # if user:
        return render(request, 'posting/save_posting.html')
        # else:
        #     return redirect('/login')


# 카테고리 별 포스팅 불러오기
def posting_list_view(request):
    # all_posting = PostingModel.objects.all()
    # {'posting': all_posting}
    return render(request, 'posting/posting_list.html')
