from django.urls import path, include
from django.urls import reverse_lazy
from accounts.views import registiration_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name='loginpage'),
    path('register/', registiration_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name="profile"),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(success_url = reverse_lazy('accounts:password_reset_done'), template_name="registration/password_reset_form.html"),
         name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]