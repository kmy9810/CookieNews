from .models import CommentModel
from django.forms import ModelForm, TextInput


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment']
        widgets = {
            'comment': TextInput(attrs={
                'class': "form-control",
                'placeholder': '댓글을 작성해 주세요.'
            }),
        }
