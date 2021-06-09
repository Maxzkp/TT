from Modulos.Atractivos.models import Atractivo,Servicio,Categoria
from django.shortcuts import render

# Create your views here.
def admin_vistaAtractivos(request):
    if request.method == 'GET':
        atractivos = Atractivo.objects.all()
        return render(request, "admin_atractivos_vista.html", {'atractivos':atractivos})

def admin_registroAtractivos(request):
    if request.method == 'GET':
        servicios = Servicio.objects.all()
        categorias=Categoria.objects.all()
        return render(request, "admin_atractivos_registrar.html",{'servicios':servicios, 'categorias':categorias})

