from django.db import models

CONDITION = (
    ("new", "New"),
    ("used", "Used"),
    ("refurbished", "Refurbished"),
)

SUPPLIER_TYPE = (
    ("verified", "Verified"),
    ("unverified", "Unverified"),
)

class CurrencyType(models.TextChoices):
    UZS = "UZS", "UZS"
    USD = "USD", "UZD"



