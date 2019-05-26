from django.db import models

from dbapp.models.Brunch import Brunch


class Article(models.Model):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    brunch = models.ForeignKey(
        Brunch,
        on_delete=models.CASCADE,
        verbose_name='Ветка'
    )
