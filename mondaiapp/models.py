from django.db import models

# Create your models here.
class Geinin(models.Model):
    neta = models.CharField( max_length=30)
    name = models.CharField( max_length=30)
    description=models.TextField(default='null')
    importance1 = models.FloatField()
    importance2 = models.FloatField()
    importance3 = models.FloatField()
    importance4 = models.FloatField()
    image = models.TextField(default='タイトル')
    Link = models.URLField()
