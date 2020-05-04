from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from PIL import Image
from .models import MediaModel

from accounts.models import Account, Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    username = forms.CharField(max_length=80)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text='', label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text='', label='Password Confirm')
    is_terms = forms.BooleanField(label='', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Account
        fields = ('email', 'username', 'fullname', 'password1', 'password2', 'is_terms')

    def clean_username(self):
        data = self.cleaned_data.get('username').replace(" ", "").lower()

        if len(data) > 5:
            print('Yapacağanız işe sokayım')
        return data


class AccountauthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


Private = (
    ('', 'Private...'),
    ('ML', 'Male'),
    ('WM', 'Woman'),
    ('PR', 'Custom')
)


class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField()
    sex = forms.ChoiceField(choices=Private, label='Private', required=False)

    class Meta:
        model = Profile
        fields = ('sex', 'profile_picture')

class SocialMediaUpdateForm(forms.ModelForm):
    class Meta:
        model = MediaModel
        fields = ('instagram', 'facebook', 'twitter', 'linkedin')
