from django.urls import path, include

from . import views

app_name = 'page'

urlpatterns = [
    path('', views.pagehome, name='homepage'),
    path('terms/', views.term_views, name='terms'),
    path('pricavy-policy/', views.privacy_views, name='privacy-policy'),
    path('privacy-statement/', views.statement_views, name='privacy-statement')
]