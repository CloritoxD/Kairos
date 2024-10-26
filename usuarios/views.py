from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirecciona a la página de login
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Buscar el usuario en la base de datos
        try:
            user_obj = User.objects.get(username=username, password=password)
            messages.success(request, 'Bienvenido, ' + user_obj.username)
            return redirect('navegando')  # Redirigir a la página principal si todo está bien
        except User.DoesNotExist:
            messages.error(request, 'Usuario o contraseña no encontrados')
    
    return render(request, 'usuarios/inicio_sesion.html')

def navegando(request):
    return render(request, 'usuarios/navegando.html')