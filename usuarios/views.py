from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def inicio_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']
        
        # Buscar el usuario en la base de datos
        try:
            usuario_obj = Usuario.objects.get(nombre_usuario=usuario, contraseña=contraseña)
            messages.success(request, 'Bienvenido, ' + usuario_obj.nombre_usuario)
            return redirect('navegando')  # Redirigir a la página principal si todo está bien
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario o contraseña no encontrados')
    
    return render(request, 'usuarios/inicio_sesion.html')

def navegando(request):
    return render(request, 'usuarios/navegando.html')