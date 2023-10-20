from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    title = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '제목을 입력하세요.',
        'style': 'width: 500px;'}),
        label='제목')
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': '내용을 입력하세요.',
                'style': 'width: 500px; height: 500px; vertical-align: top;'}), 
        label='내용')
    class Meta:
        model = Board
        fields = ('title', 'content', 'image')

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=200, label='댓글')
    class Meta:
        model = Comment
        fields = ('content', )