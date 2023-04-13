from django.shortcuts import render, redirect
from .models import BookmarkModel
from posting.models import PostingModel
from datetime import datetime


def save_bookmark_view(request, id):
    if request.method == 'GET':
        user = request.user
        post = PostingModel.objects.get(id=id)  #게시글 아이디
        bookmark_check = BookmarkModel.objects.filter(author_id=user.id, posting_id=id)
        if not bookmark_check:
            my_bookmark = BookmarkModel()
            my_bookmark.author = user
            my_bookmark.posting = post
            my_bookmark.save()
            return redirect(f"/detail-posting/{id}")  # 디테일 페이지 머무르기
        else:
            bookmark_check.delete()
            return redirect('/')


def bookmark_view(request, id):
    if request.method == 'GET':
        my_bookmark = BookmarkModel.objects.filter(author_id=request.user.id)
        return render(request, 'bookmark/bookmark.html', {'bookmark': my_bookmark})