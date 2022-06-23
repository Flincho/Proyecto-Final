from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.models import Avatar


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', min_length=3)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )
