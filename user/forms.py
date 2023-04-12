from .models import UserModel
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, Textarea, DateField


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'comment', 'imgUrl', 'blog']

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
            'imgUrl': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'imgUrl'
            }),
            'blog': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'blog'
            })
        }
