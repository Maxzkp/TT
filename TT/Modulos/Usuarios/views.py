from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.conf import settings

# Create your views here.
def admin_vista(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        capturistas = usuarios.filter(groups__name__in=['Capturista'])
        turistas = usuarios.filter(groups__name__in=['Turista'])
        usuarios = capturistas | turistas
        return render(request, "admin_usuarios_vista.html", {'usuarios':usuarios})
    elif request.method == 'POST':
        
        return admin_bloquearUsuario(request)

def admin_bloquearUsuario(request):
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

        if User.objects.filter(email=request.POST['email']).count() != 0:
            messages.add_message(request, messages.ERROR, 'Ya hay un usuario con ese correo electronico')
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
    if request.method == 'GET':
        user = User.objects.filter(id=request.GET['usr']).first()
        return render(request, "turista_usuarios_cambiarContaseña.html", {'usr':user})
    elif request.method == 'POST':
        user = User.objects.filter(id=request.POST['usrp']).first()
        if check_password(request.POST['origPass'], user.password ):
            
            try:
                validate_password(request.POST['newPass'], user)
            except ValidationError as errors:
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
                return render(request, "turista_usuarios_cambiarContaseña.html", {'usr':user})
            
            if request.POST['newPass'] != request.POST['passConf']:
                messages.add_message(request, messages.ERROR, 'Las contraseñas no coinciden')
                return render(request, "turista_usuarios_cambiarContaseña.html", {'usr':user})
            
            user.set_password(request.POST['newPass'])
            user.save()
            return redirect('/lista_usuarios/')

        else:
            messages.add_message(request, messages.ERROR, 'La contraseña original no es correcta')
            return render(request, "turista_usuarios_cambiarContaseña.html", {'usr':user})

def turista_recuperarContraseña(request):
    if request.method == 'GET':
        return render(request, "turista_usuarios_recuperarContraseña.html")
    elif request.method == 'POST':
        if request.POST['email'] == '':
            messages.add_message(request, messages.ERROR, 'No se ingreso una direccion de correo')
            return redirect('recuperar_contraseña')

        try:
            validate_email(request.POST['email'])
        except ValidationError as errors:
            for error in errors:
                    messages.add_message(request, messages.ERROR, error)
            return redirect('recuperar_contraseña')
        
        user = User.objects.filter(email=request.POST['email']).first()
        new_pass = User.objects.make_random_password()
        user.set_password(new_pass)
        user.save()
        send_recoverEmail(user.email, new_pass)
        return redirect('lista_usuarios')

def send_recoverEmail(email, passwd):
    template = get_template('correo_usuarios_recuperarContraseña.html')
    content = template.render({'pass':passwd})

    mail = EmailMultiAlternatives(
        'Recuperacion de contraseña',
        'Correo de recuperacion de contraseña',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    mail.send()