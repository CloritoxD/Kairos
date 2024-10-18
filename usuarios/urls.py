from django.urls import path
from . import views

urlpatterns = [
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('navegando/', views.navegando, name='navegando'),
]