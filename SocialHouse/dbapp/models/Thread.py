from django.db import models


class Thread(models.Model):
    class Meta:
        verbose_name = 'Тред'
        verbose_name_plural = 'Тред'

    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )

    active = models.BooleanField(
        verbose_name='Активный'
    )

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
