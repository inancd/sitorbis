from django.urls import path
from accounts.views import registiration_view, login_view, logout_view, profile_view

app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name='loginpage'),
    path('register/', registiration_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name="profile"),
]