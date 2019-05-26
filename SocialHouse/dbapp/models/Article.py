from django.contrib.auth.models import User
from django.db import models

from dbapp.models.Brunch import Brunch


class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статья'

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    brunch = models.ForeignKey(
        Brunch,
        on_delete=models.CASCADE,
        verbose_name='Ветка'
    )

    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    text = models.CharField(
        max_length=32768,
        verbose_name='Текст'
    )

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)