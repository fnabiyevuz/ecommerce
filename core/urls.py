from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .schema import swagger_urlpatterns


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean(self):
        cleaned_data = super().clean()
        captcha = cleaned_data.get("captcha")
        if not captcha:
            raise forms.ValidationError("Invalid captcha")
        return cleaned_data


admin.site.login_form = LoginForm
admin.site.login_template = "login.html"


urlpatterns = [
    path("", lambda request: redirect("admin:index")),
    re_path(r"^rosetta/", include("rosetta.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.urls")),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += [path("i18n/", include("django.conf.urls.i18n"))]


urlpatterns += swagger_urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
