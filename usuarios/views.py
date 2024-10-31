from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate  # Asegúrate de que 'logout' esté aquí
from django.shortcuts import render, redirect
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Validaciones adicionales
        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return render(request, 'usuarios/register.html')
            
        if not any(c.isupper() for c in password):
            messages.error(request, 'La contraseña debe contener al menos una letra mayúscula.')
            return render(request, 'usuarios/register.html')
            
        if not any(c.isdigit() for c in password):
            messages.error(request, 'La contraseña debe contener al menos un número.')
            return render(request, 'usuarios/register.html')
        
        # Verificar formato de email
        if '@' not in email or '.' not in email:
            messages.error(request, 'Por favor, ingrese un email válido.')
            return render(request, 'usuarios/register.html')
            
        # Verificar si el email ya existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email ya está registrado.')
            return render(request, 'usuarios/register.html')
        
        # Crear nuevo usuario
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido/a!')
            return redirect('menu_principal')
        except Exception as e:
            print(f"Error al crear el usuario: {e}")  # Imprimir el error en la consola
            messages.error(request, 'Error al crear el usuario: ' + str(e))
            return render(request, 'usuarios/register.html')
            
    return render(request, 'usuarios/register.html')

def inicio_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Cambiar username por email en el formulario
        password = request.POST.get('password')
        
        try:
            # Buscar el usuario por email
            user = User.objects.get(email=email)
            # Autenticar usando el username encontrado
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('menu_principal')
            else:
                messages.error(request, 'Email o contraseña incorrectos')
        except User.DoesNotExist:
            messages.error(request, 'No existe una cuenta con este email')
            
    return render(request, 'usuarios/inicio_sesion.html')

def navegando(request):
    return render(request, 'usuarios/navegando.html')

def menuprincipal(request):
    return render(request, 'usuarios/menu_principal.html')

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('inicio_sesion')  # Redirige a la página de inicio de sesión o a donde desees