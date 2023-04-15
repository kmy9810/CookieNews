from django.shortcuts import render, redirect
from .models import PostingModel
from bookmark.models import BookmarkModel
from comment.models import CommentModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .forms import PostingForm, CustomPostingChangeForm



@login_required
def save_posting(request):
    if request.method == 'POST':
        post = request.POST
        posting_category = post.get('posting_category')
        posting_title = post['posting_title']
        posting_content = post['posting_content']
        posting_author = request.user
        posting_video = post['posting_video']

        # https://

        # posting_video = 'https://www.youtube.com/embed/' + posting_video.split('=')[1]
        # print(posting_video)

        # if posting_title == '' or posting_category == '' or posting_content == '':
        # return render(request, 'posting/save_posting.html', {'error': '빈칸을 입력해 주세요.'})
        # pass
        if request.FILES:
            my_img = request.FILES
            PostingModel.objects.create(
                posting_category=posting_category,
                posting_title=posting_title,
                posting_content=posting_content,
                posting_author=posting_author,
                posting_img=my_img['posting_img'],
                posting_video=posting_video
            )
        else:
            PostingModel.objects.create(
                posting_category=posting_category,
                posting_title=posting_title,
                posting_content=posting_content,
                posting_author=posting_author,
                posting_img=None,
                posting_video=posting_video
            )


        return redirect('/')

    elif request.method == "GET":
        posting_form = PostingForm()  # 유저 폼을 가져옴
        return render(request, 'posting/save_posting.html', {'posting_form': posting_form})  # posting_form 이름으로 폼을 보내줌


# 카테고리 별 포스팅 불러오기
def posting_list_view(request, id):
    all_posting = PostingModel.objects.filter(posting_category=id).order_by('-id')

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
    if request.method == 'GET':
        user = request.user
        post = PostingModel.objects.get(id=id)
        bookmark = BookmarkModel.objects.filter(author_id=request.user.id, posting_id=id)
        return render(request, 'posting/detail_posting.html', {'user': user, 'post': post, 'bookmark': bookmark})
    elif request.method == 'POST':
        my_comment = CommentModel()
        my_comment.author = request.user
        my_comment.posting = PostingModel.objects.get(id=id)
        my_comment.comment = request.POST.get('comment', '')
        my_comment.save()
        return redirect(f'/detail-posting/{id}')



def delete_posting(request, id):
    post = PostingModel.objects.get(id=id)
    post.delete()
    return redirect('/')


def edit_posting(request, id):
    if request.method == 'GET':
        posting_form = PostingForm(instance=PostingModel.objects.get(id=id))  # 유저 폼을 가져옴
        return render(request, 'posting/edit_posting.html', {'posting_form': posting_form})
        #return render(request, '/edit_posting.html/', {'posting_form': posting_form})  # posting_form이란 이름으로 폼을 보내줌

    elif request.method == 'POST':
        update_form = PostingForm(request.POST, request.FILES, instance=PostingModel.objects.get(id=id))
        print('hi')
        if update_form.is_valid():
            update_form.save()
            return redirect('/')