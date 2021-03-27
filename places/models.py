from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Описание')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Локация', related_name='images')
    position = models.PositiveIntegerField('Позиция', default=0, blank=False, null=False)
    file = models.ImageField('Файл изображения')

    def __str__(self):
        return f'{self.position} {self.place}'

    class Meta:
        ordering = ['position']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
