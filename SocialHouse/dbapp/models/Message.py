from django.contrib.auth.models import User
from django.db import models
from dbapp.models.Article import Article


class Message(models.Model):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name='Статья',
        related_name='messages'
    )

    text = models.TextField(
        max_length=1024,
        verbose_name='Текст'
    )

    posted = models.DateTimeField(
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return '{}. {} {}...'.format(self.id, str(self.author), self.text[:10])
