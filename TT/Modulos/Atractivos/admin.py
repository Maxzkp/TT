from .models import Atractivo, Categoria, Horario, Servicio, Tipo, Zona, horario_atractivo
from django.contrib import admin

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Zona)
admin.site.register(Categoria)
admin.site.register(Servicio)
admin.site.register(Atractivo)
admin.site.register(Horario)
admin.site.register(horario_atractivo)