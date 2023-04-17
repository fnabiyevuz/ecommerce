from django.urls import path

from .api_endpoints import auth, profile

urlpatterns = [
    path("register/", auth.AccountRegisterView.as_view(), name="register"),
    path("login/", auth.LoginView.as_view(), name="login"),
    path("set-password/<int:pk>/", profile.SetNewPasswordView.as_view()),
    path("profile/<int:pk>/", profile.GetProfileView.as_view()),
]
