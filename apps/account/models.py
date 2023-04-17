from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from .manager import AccoutManager


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, db_index=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, verbose_name="username")
    phone_number = PhoneNumberField(region="UZ", unique=True, verbose_name="phone number")
    firstname = models.CharField(max_length=30, blank=True, null=True, verbose_name="Full name")

    # required
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "firstname"]

    objects = AccoutManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return data

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = "Accounts"


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def full_address(self):
        return f"{self.city} {self.state}"

    class Meta:
        verbose_name = _("UserProfile")
        verbose_name_plural = _("UserProfile")
        ordering = ["-id"]
