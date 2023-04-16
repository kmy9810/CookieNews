from django.shortcuts import render, redirect
from .models import BookmarkModel
from posting.models import PostingModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime


def save_bookmark_view(request, id):
    if request.method == 'GET':
        user = request.user
        post = PostingModel.objects.get(id=id)  #게시글 아이디
        bookmark_check = BookmarkModel.objects.filter(author_id=user.id, posting_id=id)  # 없으면 false?
        if not bookmark_check:
            my_bookmark = BookmarkModel()
            my_bookmark.author = user
            my_bookmark.posting = post
            my_bookmark.save()
            return redirect(f"/detail-posting/{id}")  # 디테일 페이지 머무르기
        else:
            bookmark_check.delete()
            return redirect(f"/detail-posting/{id}")


def bookmark_view(request, id):
    if request.method == 'GET':
        my_bookmark = BookmarkModel.objects.filter(author_id=id)

        page = request.GET.get('page')
        paginator = Paginator(my_bookmark, 3)
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
        return render(request, 'bookmark/bookmark.html', {'page_obj': page_obj, 'paginator': paginator,
                                                          'custom_range': custom_range})
