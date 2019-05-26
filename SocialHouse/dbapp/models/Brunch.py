from django.db import models

from dbapp.models.Thread import Thread


class Brunch(models.Model):
    class Meta:
        verbose_name = 'Ветка'
        verbose_name_plural = 'Ветки'

    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        verbose_name='Тред'
    )

    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    description = models.CharField(
        max_length=4096,
        verbose_name='Описание'
    )

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
