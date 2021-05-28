from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
class Tipo(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

class Zona(models.Model):
    descripcion = CharField(max_length=50)

class Categoria(models.Model):
    descripcion = CharField(max_length=50)

class Servicio(models.Model):
    descripcion = CharField(max_length=50)

class Atractivo(models.Model):
    tipo = ForeignKey(Tipo, on_delete=CASCADE)
    zona = ForeignKey(Zona, on_delete=CASCADE)
    categorias = ManyToManyField(Categoria)
    servicios = ManyToManyField(Servicio)
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=600)
    lat = IntegerField()
    lon = IntegerField()

class Horario(models.Model):
    inicio = TimeField()
    final = TimeField()
    descripcion = CharField(max_length=100)

class horario_atractivo(models.Model):
    atractivo = ForeignKey(Atractivo)
    horario = ForeignKey(Horario)
    dias = IntegerField()