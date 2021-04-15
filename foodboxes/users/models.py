from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    address = models.CharField('Адрес', max_length=256)
