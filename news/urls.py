from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.Page, name='page'),

    path('<slug:news_slug>/', views.Detail, name='detail'),

    path('category/<slug>', views.CategoryDetail, name='catdetail'),


]