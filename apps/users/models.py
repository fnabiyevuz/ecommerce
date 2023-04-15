from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel


# Create your models here.
class User(AbstractUser, BaseModel):
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True)
    avatar = models.ImageField(upload_to="users/%Y/%m/", blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.username:
            return str(self.username)
        if self.phone:
            return self.phone

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
