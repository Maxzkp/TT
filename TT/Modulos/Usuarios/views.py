from django.core.checks import messages
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
        #render(request, "admin_usuarios_vista.html", {'usuarios':usuarios})

def turista_registrar(request):
    contextDict = {
        'name':'',
        'email':'',
        'name_err':'',
        'email_err':'',
        'passwd_err':'',
        'pconfirm_err':''
    }
    if request.method == 'GET':
        return render(request, "turista_usuarios_registrar.html", contextDict)
    elif request.method == 'POST':
        #Crear Usuario
        usuario_nuevo = User(username=request.POST['name'], email=request.POST['email'])

        #Validar y añadir contraseña
        try:
            validate_password(request.POST['pass'])
        except ValidationError as e:
            pass
        if request.POST['pass'] == request.POST['passConf']:
            usuario_nuevo.set_password(request.POST['pass'])
        
        #Validar el objeto con el modelo
        usuario_nuevo.full_clean()
        try:
            usuario_nuevo.full_clean()
            usuario_nuevo.save()
            usuario_nuevo.groups.add(Group.objects.filter(name='Turista').first())
            return redirect('lista_usuarios')
        except ValidationError as e:
            contextDict['name'] = request.POST['name']
            contextDict['email'] = request.POST['email']
            msg = e
            return render(request, "turista_usuarios_registrar.html", contextDict)

def turista_recuperarContraseña(request):
    return render(request, "turista_usuarios_recuperarContraseña.html")