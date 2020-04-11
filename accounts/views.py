from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from accounts.forms import RegistrationForm, AccountauthenticationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from PIL import Image
# Create your views here.

def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect("blog:index")

    if request.POST:
        form = AccountauthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('blog:index')
    else:
        form = AccountauthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)

def registiration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.success(request, f'Account created for {email}!')
            return redirect('blog:index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'accounts/signup.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, f'You have successfully logged out.')
    return redirect('blog:index')

@login_required
def profile_view(request):
    if request.method == 'POST':
        query = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if query.is_valid():
            query.save()
            return redirect('accounts:profile')

    else:
        query = ProfileForm(instance=request.user.profile)
    context = {
        'query': query
    }

    return render(request, 'accounts/profile.html', context)
