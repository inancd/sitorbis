from django.urls import path
from accounts.views import registiration_view, login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='loginpage'),
    path('register/', registiration_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]