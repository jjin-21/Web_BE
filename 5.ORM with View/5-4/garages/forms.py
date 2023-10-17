from django import forms
from .models import Garage

class GarageForm(forms.ModelForm):
    location = forms.CharField(max_length=200, label='위치', widget=forms.TextInput(attrs={'class': 'form-control'}))
    capacity = forms.IntegerField(label='주차 가능 차량 수', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_parking_avaliable = forms.ChoiceField(
        label='주차 가능 여부',
        choices=((True, '가능'), (False, '불가능')),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input form-check-inline'})
    )
    opening_time = forms.TimeField(
        label='여는 시간',
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
    closing_time = forms.TimeField(
        label='닫는 시간',
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
        
    class Meta:
        model = Garage
        fields = '__all__'
