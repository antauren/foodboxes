from django.db import models


class Item(models.Model):
    title = models.CharField('Наименование')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение')
    weight = models.PositiveSmallIntegerField('Вес в граммах')
    price = models.DecimalField('Цена в рублях')
