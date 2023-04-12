from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from posting.models import PostingModel


def home(request):
    # all_posting = PostingModel.objects.all().order_by('-created')
    # page = request.GET.get('page')
    #
    # paginator = Paginator(all_content, 1)
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:  # page 숫자가 없을 시
    #     page = 1
    #     page_obj = paginator.page(page)
    # except EmptyPage:  # page 숫자가 너무 클 시 마지막 페이지를 보여줌
    #     page = paginator.num_pages
    #     page_obj = paginator.page(page)
    #
    # # 앞으로 2개 뒤로 2개 총 5개가 기본적으로 보이는 pagination
    # left_index = (int(page) - 2)
    # if left_index < 1:
    #     left_index = 1
    #
    # right_index = (int(page) + 2)
    # if right_index > paginator.num_pages:
    #     right_index = paginator.num_pages
    #
    # custom_range = range(left_index, right_index + 1)
    # {'posting': all_posting, , 'page_obj': page_obj, 'paginator': paginator, 'custom_range': custom_range}
    return render(request, 'home.html')


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            my_form = UserForm()  # 유저 폼을 가져옴
            return render(request, 'user/signup.html', {'user_form': my_form})  # form이란 이름으로 유저 폼을 보내줌

    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():  # 폼이 유효성 검사를 통과 했는가?
            my_form = request.POST  # 폼에서 전송한 데이터를 딕셔너리 형태로 전부 가져옴
            if my_form['password'] != my_form['password2']:
                return render(request, 'user/signup.html')
            else:
                exist_user = get_user_model().objects.filter(username=my_form['username'])
                if exist_user:
                    return render(request, 'user/signin.html')
                else:
                    user = UserModel.objects.create_user(username=my_form['username'], password=my_form['password'],
                                                          birth=my_form['birth'], imgUrl=my_form['imgUrl'],
                                                          blog=my_form['blog'], comment=my_form['comment'])
                                                            # 폼의 key값으로 value를 찾아봅시다~
                    auth.login(request, user)  # 로그인 시켜서 홈으로~
                    return redirect('/')


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


def profile_view(request, id):
    if request.method == 'GET':
     a = UserModel.request.POST.get('id', None)
     print(a)
    return redirect('/profile')

