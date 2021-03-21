from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Описание')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Локация", related_name="images")
    position = models.IntegerField('Позиция', blank=True)
    file = models.ImageField('Файл изображения')

    def __str__(self):
        return f'{self.position} {self.place}'
