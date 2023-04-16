from django.shortcuts import render, redirect
from .models import CommentModel
from .forms import CommentForm
from posting.models import PostingModel
from bookmark.models import BookmarkModel
# Create your views here.


def delete_comment(request, id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    return redirect(f'/detail-posting/{comment.posting_id}')


def edit_comment(request, id):
    print(id)
    if request.method == 'POST':
        update_form = request.POST.get('comment', '')
        my_comment = CommentModel.objects.get(id=id)
        my_comment.comment = update_form + '(수정됨)'
        my_comment.save()
        return redirect(f'/detail-posting/{my_comment.posting.id}')
