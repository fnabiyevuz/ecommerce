from django.urls import path

from .api_endpoints import auth, profile

app_name = "account"

urlpatterns = [
    path("register/", auth.AccountRegisterView.as_view(), name="register"),
    path("login/", auth.LoginView.as_view(), name="login"),
    path("set-password/", profile.SetNewPasswordView.as_view(), name="set-password"),
    path("profile-get/<int:pk>/", profile.GetProfileView.as_view(), name="profile-get"),
    path("profile-delete/", profile.DeleteProfileView.as_view(), name="profile-delete"),
    path("like-product/<int:product>/", profile.YouLikeProductCreate.as_view(), name="like-product"),
    path("like-product-get/", profile.YouLikeProductGet.as_view(), name="like-product-get"),
]
