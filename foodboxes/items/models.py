from django.db import models


class Item(models.Model):
    title = models.CharField('Наименование', max_length=256)
    description = models.TextField('Описание', max_length=1000)
    image = models.ImageField('Изображение')
    weight = models.PositiveSmallIntegerField('Вес в граммах')
    price = models.DecimalField('Цена в рублях', max_digits=10, decimal_places=2)
