from django.shortcuts import render, redirect, HttpResponse
from .models import UserModel
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserForm, CustomUserChangeForm
from posting.models import PostingModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    all_posting = PostingModel.objects.all().order_by('-posting_created')
    page = request.GET.get('page')
    paginator = Paginator(all_posting, 3)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:  # page 숫자가 없을 시
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:  # page 숫자가 너무 클 시 마지막 페이지를 보여줌
        page = paginator.num_pages
        page_obj = paginator.page(page)

    # 앞으로 2개 뒤로 2개 총 5개가 기본적으로 보이는 pagination
    left_index = (int(page) - 2)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    custom_range = range(left_index, right_index + 1)

    return render(request, 'home.html', {'page_obj': page_obj, 'paginator': paginator, 'custom_range': custom_range})


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            my_form = UserForm()  # 유저 폼을 가져옴
            return render(request, 'user/signup.html', {'form': my_form})  # form이란 이름으로 유저 폼을 보내줌

    elif request.method == 'POST':
        form = UserForm(request.POST)
        my_form = {k: v[0] if isinstance(v, list) else v for k, v in request.POST.items() if
                   k not in ["csrfmiddlewaretoken"]}  # 폼에서 전송한 데이터를 딕셔너리 형태로 전부 가져옴
        exist_user = get_user_model().objects.filter(username=request.POST.get('username', ''))
        if my_form['password'] != my_form.pop('password2', ""):
            return HttpResponse('비밀번호가 서로 일치하지 않습니다!')
        elif exist_user:
            return render(request, 'user/signin.html')
        else:
            if form.is_valid():  # 폼이 유효성 검사를 통과 했는가?
                my_form['imgUrl'] = request.FILES.get('imgUrl') or ""
                user = UserModel.objects.create_user(**my_form)
                auth.login(request, user)  # 로그인 시켜서 홈으로~
                return redirect('/')
            else:
                return HttpResponse('형식이 올바르지 않습니다!')


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


@login_required
def profile_view(request):
    return render(request, 'user/profile.html')


@login_required
def delete_user_view(request):
    user = request.user
    user.delete()
    auth.logout(request)
    return redirect('/')


@login_required
def edit_user_view(request):
    if request.method == 'GET':
        user_form = CustomUserChangeForm(instance=request.user)
        return render(request, 'user/edituser.html', {'form': user_form})

    elif request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('/profile/')


def user_posting_view(request):
    if request.method == 'GET':
        my_posting = PostingModel.objects.filter(posting_author=request.user).order_by('-posting_created')

        page = request.GET.get('page')
        paginator = Paginator(my_posting, 5)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:  # page 숫자가 없을 시
            page = 1
            page_obj = paginator.page(page)
        except EmptyPage:  # page 숫자가 너무 클 시 마지막 페이지를 보여줌
            page = paginator.num_pages
            page_obj = paginator.page(page)

        # 앞으로 2개 뒤로 2개 총 5개가 기본적으로 보이는 pagination
        left_index = (int(page) - 2)
        if left_index < 1:
            left_index = 1

        right_index = (int(page) + 2)
        if right_index > paginator.num_pages:
            right_index = paginator.num_pages

        custom_range = range(left_index, right_index + 1)
        return render(request, 'user/user_all_posting.html',
                      {'page_obj': page_obj, 'paginator': paginator, 'custom_range': custom_range})


def delete_user_posting_view(request, id):
    post = PostingModel.objects.get(id=id)
    post.delete()
    return redirect('/user-posting/')
