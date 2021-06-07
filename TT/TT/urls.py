"""TT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Modulos.Usuarios.views import admin_vista, turista_recuperarContraseña, turista_registrar, turista_cambiarContraseña
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_usuarios/', admin_vista, name='lista_usuarios'),
    path('registro/', turista_registrar, name='registro'),
    path('cambiar_contraseña/', turista_cambiarContraseña, name='cambiar_contraseña'),
    path('recuperar_contraseña/', turista_recuperarContraseña, name='recuperar_contraseña'),
]
