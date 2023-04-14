from .models import UserModel
from django.forms import ModelForm, TextInput, PasswordInput, \
    EmailInput, Textarea, FileInput, NumberInput
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'comment', 'blog', 'imgUrl', 'birth']

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
                'placeholder': 'Password'
            }),
            'comment': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'comment'
            }),
            'blog': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'blog'
            }),
            'imgUrl': FileInput(attrs={
                'class': "form-control"
            }),
            'birth': NumberInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = UserModel
        fields = ['email', 'comment', 'blog']
