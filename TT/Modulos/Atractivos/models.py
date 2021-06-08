from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField

# Create your models here.
class Tipo(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.descripcion

class Zona(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.descripcion

class Servicio(models.Model):
    descripcion = CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.descripcion

class Atractivo(models.Model):
    tipo = OneToOneField(Tipo, on_delete=CASCADE, blank=False)
    zona = OneToOneField(Zona, on_delete=CASCADE, blank=False)
    categorias = ManyToManyField(Categoria, blank=False)
    servicios = ManyToManyField(Servicio, blank=False)
    nombre = CharField(max_length=100, null=False, blank=False)
    direccion = CharField(max_length=100, null=False, blank=False)
    descripcion = CharField(max_length=600, null=False, blank=False)

    def __str__(self):
        return self.nombre

    

class Horario(models.Model):
    inicio = TimeField()
    final = TimeField()
    descripcion = CharField(max_length=100, null=False, blank=False)

class horario_atractivo(models.Model):
    atractivo = OneToOneField(Atractivo, on_delete=CASCADE, blank=False)
    horario = OneToOneField(Horario, on_delete=CASCADE, blank=False)
    dias = IntegerField(null=False, blank=False)