from django.db import models

# Create your models here.


class Avideo(models.Model):
    COUNTRY = (('JAP', 'Janpen'), ('Chi','China'), ('Kor','Korea'), ('USA', 'Unite states'))
    name = models.CharField(max_length=100, verbose_name='avideo name')
    media_file = models.FileField()
    actor_name = models.CharField(max_length=100, verbose_name='actor name')
    country = models.CharField(max_length=100, verbose_name='countryname', choices= COUNTRY)

    def __str__(self):
        return self.name
    pass

class Video(models.Model):
    pass

class LiveVideo(models.Model):
    pass
