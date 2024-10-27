from django.urls import path
from .views import registro, inicio_sesion, navegando, menuprincipal , logout_view

urlpatterns = [
    path('registro/', registro, name='register'),  # URL para el registro
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('navegando/', navegando, name='navegando'),
    path('menu_principal/', menuprincipal, name='menu_principal'),
    path('logout/', logout_view, name='logout'),  # Asegúrate de que este nombre coincida
]