from django.db import models


class CartStatusType(models.TextChoices):
    NEW = "NEW", "New"
    ORDERED = "ORDERED", "Ordered"
