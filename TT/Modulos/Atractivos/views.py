from Modulos.Atractivos.models import Atractivo
from django.shortcuts import render

# Create your views here.
def admin_vistaAtractivos(request):
    if request.method == 'GET':
        atractivos = Atractivo.objects.all()
        return render(request, "admin_atractivos_vista.html", {'atractivos':atractivos})

def admin_registroAtractivos(request):
    return render(request, "admin_atractivos_registrar.html")        