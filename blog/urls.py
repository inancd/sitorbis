from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Page, name='index'),
    path('<slug:slug>/', views.Detail_view, name="detail"),
    path('category/<slug:slug>/', views.Category_view, name="category"),
    path('like', views.like_post, name="like_post"),

]

