from django.db import models


class CouponType(models.TextChoices):
    PERCENT = "PERCENT", "Percent"
    FIXED = "FIXED", "Fixed"


class OrderStatusType(models.TextChoices):
    NEW = "NEW", "New"
    IN_PROCESS = "IN_PROCESS", "In-process"
    ACCEPTED = "ACCEPTED", "Accepted"
    CANCELLED = "CANCELLED", "Cancelled"


class PaymentType(models.TextChoices):
    CASH = "CASH", "Cash"
    CLICK = "CLICK", "Click"
    PAYME = "PAYME", "Payme"
    UZUM_BANK = "UZUM_BANK", "Uzum Bank"
