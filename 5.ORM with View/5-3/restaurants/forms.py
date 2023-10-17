from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='이름', widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    description = forms.CharField(
        max_length=250, label='식당 소개',
        widget=forms.Textarea(attrs={'style': 'width: 100%; height: 150px;'}),
        help_text='주소는 OO시 OO구 OO동 형식으로 작성합니다.',
    )
    address = forms.CharField(label=' 주소', widget=forms.TextInput(attrs={'style': 'width: 100%'}))
    phone_number = forms.CharField(
        label='전화번호',
        widget=forms.TextInput(attrs={'style': 'width: 100%'}),
        help_text='전화번호는 특수문자 없이 지역번호를 포함한 숫자만 입력합니다.',
    )
    class Meta():
        model = Restaurant
        fields = '__all__'