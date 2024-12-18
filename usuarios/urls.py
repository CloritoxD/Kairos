from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='register'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/', views.logout_view, name='logout'), 
    path('navegando/', views.navegando, name='navegando'),
    path('menu_principal/',views.menuprincipal, name='menu_principal'),
    path('productos/', views.productos, name='productos'),
    path('solicitar-garantia/<int:producto_id>/', views.solicitar_garantia, name='solicitar_garantia'),
    path('menupqr', views.pqr_home, name='pqr_home'),
    path('crear/<str:tipo>/', views.crear_solicitud, name='crear_solicitud'),
 # formulario_reclamo
    path('formulario_reclamo/<str:tipo>/', views.formulario_reclamo, name='formulario_reclamo'),
    path('formulario_peticion/<str:tipo>/', views.formulario_peticion, name='formulario_peticion'),
    path('formulario_queja/<str:tipo>/', views.formulario_queja, name='formulario_queja'),
]