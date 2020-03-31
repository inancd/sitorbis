from django import forms
from .models import Comment
from django.conf import settings

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)