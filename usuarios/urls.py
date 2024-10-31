from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='register'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/', views.logout_view, name='logout'), 
    path('navegando/', views.navegando, name='navegando'),
    path('menu_principal/',views.menuprincipal, name='menu_principal'),
]