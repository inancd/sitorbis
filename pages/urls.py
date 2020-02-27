from django.urls import path, include

from . import views

app_name = 'page'

urlpatterns = [
    path('', views.pagehome, name='homepage')
]