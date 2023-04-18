from django.db import models

CONDITION = (
    ("new", "New"),
    ("used", "Used"),
    ("refurbished", "Refurbished"),
)


class CurrencyType(models.TextChoices):
    UZS = "UZS", "UZS"
    USD = "USD", "UZD"
