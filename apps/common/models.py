from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class Region(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class District(models.Model):
    region = models.ForeignKey(Region, verbose_name=_('Region'), on_delete=models.CASCADE,
                               related_name='district_regions')
    name = models.CharField(verbose_name=_('Name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"
