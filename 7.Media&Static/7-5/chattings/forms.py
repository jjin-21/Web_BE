<<<<<<< HEAD
from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    user = forms.CharField(
        max_length=10,
        label = '작성자',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nickname',
            }
        )
    )
    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs={
                'placeholder':'Chat!',
                'rows':5,
                'cols':50,
            }
        ))
    class Meta:
        model = Chat
=======
from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    user = forms.CharField(
        max_length=10,
        label = '작성자',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nickname',
            }
        )
    )
    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs={
                'placeholder':'Chat!',
                'rows':5,
                'cols':50,
            }
        ))
    class Meta:
        model = Chat
>>>>>>> 839d8730f0ca103e47c95ab8477c42cb69f4f5e6
        fields = "__all__"