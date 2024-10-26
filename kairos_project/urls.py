from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Asegúrate de que esta línea incluye los URLs de la app usuarios
    path('', lambda request: redirect('inicio_sesion')),  # Redirigir la ruta principal
]
