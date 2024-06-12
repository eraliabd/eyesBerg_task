from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


class CustomUserGenderChoice(models.TextChoices):
    MALE = "male"
    FEMALE = "female"


class CustomUser(AbstractUser, PermissionsMixin):
    _validate_phone = RegexValidator(
        regex=r'^998[0-9]{9}$',
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan iborat bo'lishi kerak. Masalan: 998901235476"
    )

    affiliation = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True, validators=[_validate_phone])
    gender = models.CharField(max_length=10, choices=CustomUserGenderChoice.choices, blank=True, null=True)

    def __str__(self):
        return self.username
