from django.contrib import admin
from .models import Usuario  # Asegúrate de que esta línea sea correcta

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario',)
