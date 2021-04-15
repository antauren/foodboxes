from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Reviews(models.Model):
    PUBLISHED = 'published'
    ON_MODERATION = 'on moderation'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (PUBLISHED, 'Опубликован'),
        (ON_MODERATION, 'На модерации'),
        (REJECTED, 'Отклонен'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    created_at = models.DateTimeField('Дата создания')
    published_at = models.DateTimeField('Дата публикации')
    status = models.CharField('Статус', choices=STATUS_CHOICES, default=ON_MODERATION, max_length=20)
