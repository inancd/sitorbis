from django.shortcuts import render


# Create your views here.

def loginApp(request):
    return render(request, 'accounts/login.html')

def signupApp(request):
    return render(request, 'accounts/signup.html')