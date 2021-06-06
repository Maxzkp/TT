from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User

# Create your views here.
def admin_vista(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        usuarios.order_by('groups__name')
        usuarios = usuarios.exclude(groups__name__in=['Superuser', 'Administrador'])
        return render(request, "admin_usuarios_vista.html", {'usuarios':usuarios})
    elif request.method == 'POST':
        usuario = User.objects.filter(id=request.POST['req'])
        if usuario.first() != None:
            usuario = usuario.first()
            usuario.is_active = not usuario.is_active
            usuario.save()
        return redirect('lista_usuarios')

def turista_registrar(request):
    if request.method == 'GET':
        return render(request, "turista_usuarios_registrar.html", {'name':'', 'email':''})

    elif request.method == 'POST':
        #Crear Usuario
        if request.POST['email'] == '':
            messages.add_message(request, messages.ERROR, 'No se ingresó un correo electronico')
            return render(request, "turista_usuarios_registrar.html", {'name':request.POST['name'].strip(), 'email':request.POST['email']})
        usuario_nuevo = User(username=request.POST['name'].strip(), email=request.POST['email'])

        #Validar y añadir contraseña
        try:
            validate_password(request.POST['pass'], usuario_nuevo)
        except ValidationError as errors:
            for error in errors:
                messages.add_message(request, messages.ERROR, error)
            return render(request, "turista_usuarios_registrar.html", {'name':request.POST['name'].strip(), 'email':request.POST['email']})

        if request.POST['pass'] != request.POST['passConf']:
            messages.add_message(request, messages.ERROR, 'Las contraseñas no coinciden')
            return render(request, "turista_usuarios_registrar.html", {'name':request.POST['name'].strip(), 'email':request.POST['email']})
        usuario_nuevo.set_password(request.POST['pass'])
        
        #Validar el objeto con el modelo
        try:
            usuario_nuevo.full_clean()
            usuario_nuevo.save()
            usuario_nuevo.groups.add(Group.objects.filter(name='Turista').first())
            return redirect('lista_usuarios')
        except ValidationError as errors:
            for error in errors:
                for e in error[1]:
                    messages.add_message(request, messages.ERROR, e)
            return render(request, "turista_usuarios_registrar.html", {'name':request.POST['name'].strip(), 'email':request.POST['email']})

def turista_cambiarContraseña(request):
    return render(request, "turista_usuarios_recuperarContraseña.html")

def turista_recuperarContraseña(request):
    return render(request, "turista_usuarios_recuperarContraseña.html")