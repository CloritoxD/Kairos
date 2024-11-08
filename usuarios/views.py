from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto, SolicitudGarantia
import random
import string
from .models import Solicitud

#-------------------------------
# Carlos Puso esto
def pqr_home(request):
    return render(request, 'usuarios/pqr_home.html')

def crear_solicitud(request, tipo):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        Solicitud.objects.create(tipo=tipo, descripcion=descripcion)
        return redirect('pqr_home')
    return render(request, 'usuarios/crear_solicitud.html', {'tipo': tipo})
#-------------------------------

def formulario_reclamo(request, tipo):
    # Your view logic here
    return render(request, 'usuarios/formulario.html', {'tipo': tipo})

#-------------------------------

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
    if not request.user.is_authenticated:
        return redirect('inicio_sesion')
    
    # Añade algunos productos de ejemplo si no existen
    if Producto.objects.count() == 0:
        productos_ejemplo = [
            {
                'nombre': 'Rolex Submariner',
                'descripcion': 'Reloj de lujo resistente al agua',
                'precio': 10000.00,
                'imagen': 'https://ejemplo.com/rolex.jpg'
            },
            {
                'nombre': 'Omega Speedmaster',
                'descripcion': 'Reloj deportivo profesional',
                'precio': 8000.00,
                'imagen': 'https://ejemplo.com/omega.jpg'
            },
            # Añade más productos si lo deseas
        ]
        
        for producto in productos_ejemplo:
            Producto.objects.create(**producto)
    
    productos = Producto.objects.all()
    context = {
        'message': f'Bienvenido, {request.user.username}',
        'productos': productos
    }
    return render(request, 'usuarios/menu_principal.html', context)

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('inicio_sesion')  # Redirige a la página de inicio de sesión o a donde desees
def generar_codigo_seguimiento():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def menuprincipal(request):
    productos = Producto.objects.all()
    return render(request, 'usuarios/menu_principal.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'usuarios/productos.html', {'productos': productos})

def solicitar_garantia(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        if producto.esta_en_garantia():
            problema = request.POST.get('problema')
            codigo = generar_codigo_seguimiento()
            
            solicitud = SolicitudGarantia.objects.create(
                usuario=request.user,
                producto=producto,
                problema=problema,
                codigo_seguimiento=codigo
            )
            messages.success(request, f'Solicitud de garantía registrada. Código de seguimiento: {codigo}')
            return redirect('menu_principal')
        else:
            messages.error(request, 'Este producto ya no está en garantía.')
    
    return render(request, 'usuarios/solicitar_garantia.html', {'producto': producto})