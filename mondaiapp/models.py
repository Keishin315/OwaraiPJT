from django.db import models

# Create your models here.
class Geinin(models.Model):
    neta = models.CharField( max_length=30)
    name = models.CharField( max_length=30)
    description=models.TextField(default='null')
    importance1 = models.FloatField(default=1)
    importance2 = models.FloatField(default=1)
    importance3 = models.FloatField(default=1)
    importance4 = models.FloatField(default=1)
    importance5 = models.FloatField(default=1)
    importance6 = models.FloatField(default=1)
    image = models.TextField(default='タイトル')
    Link = models.URLField()
