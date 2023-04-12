from django.shortcuts import render, redirect
import posting.models
from .models import PostingModel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     user = request.user.is_authenticated # 로그인 여부
#     if user:
#         return redirect('/save-posting')
#     else:
#         return redirect('/')


#@login_required
def save_posting(request):
    if request.method == 'POST':
        posting_category = request.POST.get('posting_category', '')
        posting_title = request.POST.get('posting_title', '')
        posting_content = request.POST.get('posting_content', '')
        posting_author = request.user

        if posting_title == '' or posting_category == '' or posting_content == '':
            #return render(request, 'posting/save_posting.html', {'error': '빈칸을 입력해 주세요.'})
            return HttpResponse("test")
        else:
            post = PostingModel.objects.create(
                posting_category=posting_category,
                posting_title=posting_title,
                posting_content=posting_content,
                posting_author=posting_author
                # 게시글 작성자 추가해야 하는지?
            )
            return HttpResponse("게시글 작성 완료!")

            # posting.save()
            # all_posting = PostingModel.objects.all()
            # render(request, 'posting/posting_list.html', {'posting': all_posting})


# 카테고리 별 포스팅 불러오기
def posting_list_view(request):
    # posting_id = request.POST.get('id', '')
    # try:
    #     post = PostingModel.objects.get(posting_id=posting_id)
    # except PostingModel.DoesNotExist:
    #     return HttpResponse("존재하지 않는 게시글입니다.")
    #
    # posting_category = request.POST.get('posting_category', '')
    # posting_title = request.POST.get('posting_title', '')
    # posting_content = request.POST.get('posting_content', '')

    if request.method == "GET":
        """게시글 조회"""
        posts = PostingModel.objects.all()
        data = []

        for p in posts:
            data.append({
                "카테고리": posting.posting_category,
                "제목": posting.posting_title,
                "내용": posting.posting_content,
            })
            """
            django rest framework 사용 시
            serializer = PostingModelSerializer(posts, many=True)
            return Response(serializer.data)
            """
        #return HttpResponse(data)

        all_posting = PostingModel.objects.all()
        {'posting': all_posting}
        return render(request, 'posting/posting_list.html', {'posting': all_posting})



def detail_posting(request):

    return render(request, 'posting/detail_posting.html')
