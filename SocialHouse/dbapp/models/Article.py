from django.contrib.auth.models import User
from django.db import models

from dbapp.models.Thread import Thread


class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статья'

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        verbose_name='Тред'
    )

    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    text = models.TextField(
        max_length=32768,
        verbose_name='Текст'
    )

    posted = models.DateTimeField(
        verbose_name='Дата публикации'
    )

    def messages_count(self):
        return self.messages.count()

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
