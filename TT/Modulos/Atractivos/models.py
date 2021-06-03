from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
class Tipo(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

class Zona(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

class Categoria(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

class Servicio(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

class Atractivo(models.Model):
    tipo = ForeignKey(Tipo, on_delete=CASCADE, null=False, blank=False)
    zona = ForeignKey(Zona, on_delete=CASCADE, null=False, blank=False)
    categorias = ManyToManyField(Categoria, null=False, blank=False)
    servicios = ManyToManyField(Servicio, null=False, blank=False)
    nombre = CharField(max_length=100, null=False, blank=False)
    descripcion = CharField(max_length=600, null=False, blank=False)

class Horario(models.Model):
    inicio = TimeField()
    final = TimeField()
    descripcion = CharField(max_length=100, null=False, blank=False)

class horario_atractivo(models.Model):
    atractivo = ForeignKey(Atractivo, primary_key=True)
    horario = ForeignKey(Horario, primary_key=True)
    dias = IntegerField(null=False, blank=False)