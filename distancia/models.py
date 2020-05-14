from django.db import models
import uuid
# Create your models here.

class Distancia(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, editable=False)
    #codigo = models.CharField(verbose_name='Codigo', primary_key=True)
    #longitud = models.CharField(verbose_name='Longitud')
    #latitud = models.CharField(verbose_name='Latitud')
    #terreno = models.CharField(verbose_name='Terreno', max_length=20)
    #area = models.IntegerField(verbose_name='Area')

    codigo = models.IntegerField(verbose_name='Codigo', primary_key=True)
    longitud = models.FloatField(verbose_name='Longitud')
    latitud = models.FloatField(verbose_name='Latitud')
    terreno = models.CharField(verbose_name='Terreno', max_length=20)
    area = models.PositiveIntegerField(verbose_name='Area')

    #type = models.CharField(verbose_name='Tipo', max_length=20)
    #value = models.IntegerField(verbose_name='Valor', )
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
