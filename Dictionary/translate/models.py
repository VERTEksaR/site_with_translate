from django.db import models


class Translate(models.Model):
    class Meta:
        verbose_name = 'Перевод'

    language_from = models.CharField(max_length=3, verbose_name='Перевод с')
    language_to = models.CharField(max_length=3, verbose_name='Перевод на')
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.language_from} --> {self.language_to}'
