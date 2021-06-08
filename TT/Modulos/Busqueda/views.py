from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.
def admin_buscarUsuarios(request):
    if request.method == 'GET':
        return redirect('lista_usuarios')
    elif request.method == 'POST':
        by_uname = User.objects.filter(username__contains=request.POST['busqueda'])
        by_mail  = User.objects.filter(email__contains=request.POST['busqueda'])
        usuarios = by_uname | by_mail
        if usuarios.count() == 0:
            messages.add_message(request, messages.ERROR, 'No se encontro ningun usuario')
        return render(request, "admin_usuarios_vista.html", {'usuarios':usuarios})