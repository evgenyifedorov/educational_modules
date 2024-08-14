from django.contrib.auth.models import AbstractUser
from django.db import models

from educmodels.models import EduModel

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    User model with additional fields for phone number and course.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=30, verbose_name="телефон", **NULLABLE)
    course = models.ForeignKey(
        EduModel, on_delete=models.CASCADE, verbose_name="курс", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
