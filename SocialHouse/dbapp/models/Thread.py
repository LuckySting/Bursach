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

    description = models.CharField(
        max_length=1024,
        verbose_name='Описание',
        default=''
    )

    image = models.FileField(
        verbose_name="Фото",
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
