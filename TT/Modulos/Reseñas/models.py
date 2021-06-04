from django.db.models.enums import Choices
from django.db.models.fields import CharField, IntegerField
from Modulos.Atractivos.models import Atractivo
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Reseña(models.Model):
    usuario = ForeignKey(User, on_delete=CASCADE, null=False, blank=False)
    atractivo = ForeignKey(Atractivo, on_delete=CASCADE, null=False, blank=False)
    evaluacion = CharField(max_length=2, choices=[(1,'1'), (2,'2'), (3, '3'), (4,'4'), (5, '5')], null=False, blank=False)
    Descripcion = CharField(max_length=600, null=False, blank=False)