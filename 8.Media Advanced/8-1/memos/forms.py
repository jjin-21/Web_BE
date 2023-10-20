<<<<<<< HEAD
from django import forms
from .models import Memo

# Create your models here.
class MemoForm(forms.ModelForm):

    summary = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder':"summary",
            }
        )
    )
    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':"memo",
                'rows':5,
                'cols':50,
            }
        )
    )

    class Meta:

        model = Memo
=======
from django import forms
from .models import Memo

# Create your models here.
class MemoForm(forms.ModelForm):

    summary = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder':"summary",
            }
        )
    )
    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':"memo",
                'rows':5,
                'cols':50,
            }
        )
    )

    class Meta:

        model = Memo
>>>>>>> 839d8730f0ca103e47c95ab8477c42cb69f4f5e6
        fields = '__all__'