from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'ex) 제주도'}))
    plan = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'ex) 여행 계획을 입력하세요'}))
    start_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'placeholder': 'ex) 2022-02-22'}))
    end_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'placeholder': 'ex) 2022-02-22'}))
    
    class Meta:
        model = Travel
        fields = '__all__'