from django.db.models.enums import Choices
from django.db.models.fields import CharField
from Modulos.Atractivos.models import Atractivo
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Reseña(models.Model):
    usuario = ForeignKey(User, on_delete=CASCADE, primary_key=True)
    atractivo = ForeignKey(Atractivo, on_delete=CASCADE, primary_key=True)
    evaluacion = Choices([1,2,3,4,5])
    Descripcion = CharField(max_length=600)