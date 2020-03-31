from django import forms
from .models import Comment
from django.conf import settings

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Your Comment'}))
    class Meta:
        model = Comment
        fields = ('content',)