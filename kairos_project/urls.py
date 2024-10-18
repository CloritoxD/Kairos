from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio_sesion/', include('usuarios.urls')),
    path('', lambda request: redirect('inicio_sesion')),  # Redirigir la ruta principal
]
