from django.shortcuts import render, redirect
import posting.models
from .models import PostingModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
# def home(request):
#     user = request.user.is_authenticated # 로그인 여부
#     if user:
#         return redirect('/save-posting')
#     else:
#         return redirect('/')


# @login_required
def save_posting(request):
    if request.method == 'POST':
        post = request.POST
        posting_category = post.get('posting_category')
        posting_title = post['posting_title']
        posting_content = post['posting_content']
        posting_author = request.user

        # if posting_title == '' or posting_category == '' or posting_content == '':
        # return render(request, 'posting/save_posting.html', {'error': '빈칸을 입력해 주세요.'})
        # pass
        PostingModel.objects.create(
            posting_category=posting_category,
            posting_title=posting_title,
            posting_content=posting_content,
            posting_author=posting_author
        )

        return redirect('/')

    elif request.method == "GET":
        """게시글 조회"""
        return render(request, 'posting/save_posting.html')


# 카테고리 별 포스팅 불러오기
def posting_list_view(request, id):
    all_posting = PostingModel.objects.filter(posting_category=id).order_by('-posting_created')

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
    return render(request, 'posting/posting_list.html', {'page_obj': page_obj, 'paginator': paginator,
                                                         'custom_range': custom_range, 'category': id})


def detail_posting(request, id):
    return render(request, 'posting/detail_posting.html')
