from .models import PostingModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm  # user프로필 수정
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput, Select


class PostingForm(ModelForm):
    class Meta:
        model = PostingModel
        fields = ['posting_category', 'posting_title', 'posting_img',
                  'posting_video',
                  'posting_content']
        categorys = (
            ('뉴스피드', '뉴스피드'),
            ('자유게시판', '자유게시판'),
        )
        widgets = {
            'posting_category': Select(choices=categorys),
            'posting_title': TextInput(attrs={
                'class': "form-control",
                'placeholder': '제목'
            }),
            'posting_img': ClearableFileInput(attrs={
                'class': "form-control",
                'placeholder': '이미지',
            }),
            'posting_video': TextInput(attrs={
                'class': "form-control",
                'placeholder': '영상 URL'
            }),
            'posting_content': Textarea(attrs={
                'class': "form-control",
                'placeholder': '내용'
            }),
        }


class CustomPostingChangeForm(UserChangeForm):
    class Meta:
        model = PostingModel
        fields = ['posting_category', 'posting_title', 'posting_img',
                  'posting_video',
                  'posting_content']
        categorys = (
            ('뉴스피드', '뉴스피드'),
            ('자유게시판', '자유게시판'),
        )
        widgets = {
            'posting_category': Select(choices=categorys),
            'posting_title': TextInput(attrs={
                'class': "form-control",
                'placeholder': '제목'
            }),
            'posting_img': ClearableFileInput(attrs={
                'class': "form-control",
                'placeholder': '이미지',
            }),
            'posting_video': TextInput(attrs={
                'class': "form-control",
                'placeholder': '영상 URL'
            }),
            'posting_content': Textarea(attrs={
                'class': "form-control",
                'placeholder': '내용'
            }),
        }
