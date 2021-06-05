from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User

# Create your views here.
def admin_vista(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        usuarios = usuarios.exclude(groups__name__in=['Superuser', 'Administrador'])
        return render(request, "admin_usuarios_vista.html", {'usuarios':usuarios})
    elif request.method == 'POST':
        usuario = User.objects.filter(username=request.POST['req'])
        if usuario.first() != None:
            usuario = usuario.first()
            usuario.is_active = not usuario.is_active
            usuario.save()
        return redirect('/lista_usuarios/') 
        #render(request, "admin_usuarios_vista.html", {'usuarios':usuarios})

def turista_registrar(request):
    return render(request, "turista_usuarios_registrar.html")

def turista_recuperarContraseña(request):
    return render(request, "turista_usuarios_recuperarContraseña.html")