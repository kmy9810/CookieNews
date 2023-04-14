from .models import UserModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm #user프로필 수정
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, Textarea


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'comment', 'blog']

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'ID'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder' : 'Password'
            }),
            'comment': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'comment'
            }),
            'blog': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'blog'
            })
        }
