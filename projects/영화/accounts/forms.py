# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='이메일 주소')
    first_name = forms.CharField(label='성', max_length=10, required=True)
    last_name = forms.CharField(label='이름', max_length=10, required=True)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label='이메일 주소')
    first_name = forms.CharField(label='성', max_length=10, required=True)
    last_name = forms.CharField(label='이름', max_length=10, required=True)
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()