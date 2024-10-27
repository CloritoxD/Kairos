from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido/a!')
            return redirect('inicio_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})  # Asegúrate de incluir "usuarios/register.html"

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Usa `get()` para evitar el error si la clave no existe
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_principal')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')
    return render(request, 'usuarios/inicio_sesion.html')

def navegando(request):
    return render(request, 'usuarios/navegando.html')

def menuprincipal(request):
    return render(request, 'usuarios/menu_principal.html')

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('inicio_sesion')  # Redirige a la página de inicio de sesión