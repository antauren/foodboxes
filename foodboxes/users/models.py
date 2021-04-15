from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField('Отчество')
    phone = models.CharField('Телефон')
    address = models.CharField('Адрес')
