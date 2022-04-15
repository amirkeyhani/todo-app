from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home/', views.home, name='home'),
    path('registration/', views.registration, name='register'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="change-password.html"), name='change-password'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name="change-password-done.html"), name='password-change-done'),
    path('account-deleted/', views.delete_account, name='delete-account'),
    path('update-profile/', views.update_profile, name='update-profile'),
]
