from django import forms
from .models import Comment, Newsletter
from django.conf import settings

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Your Comment'}))
    class Meta:
        model = Comment
        fields = ('content',)


class NewsletterCreateForm(forms.ModelForm):
    newsletter = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control strbs-footer-newsletter__form', 'placeholder': 'Email Adress'}))
    class Meta:
        model = Newsletter
        fields = '__all__'

