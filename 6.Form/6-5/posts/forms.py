from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'style': 'width: 100%; resize: vertical;'})
    )
    
    class Meta():
        model = Post
        fields = '__all__'