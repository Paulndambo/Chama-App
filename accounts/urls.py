from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html")),
    path("logout/", auth_views.LogoutView.as_view()),
]


#accounts/login/ [name='login']
#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']
