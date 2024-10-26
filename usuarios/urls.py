from django.urls import path
from .views import register_view, inicio_sesion, navegando

urlpatterns = [
    path('registro/', register_view, name='register'),  # URL para el registro
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('navegando/', navegando, name='navegando'),
]