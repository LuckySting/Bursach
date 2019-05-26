from django.db import models


class Message(models.Model):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    Article = models.ForeignKey(
        Article
    )