from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Page, name='index'),
    path('<slug:slug>/', views.Detail_view, name="detail")
]

