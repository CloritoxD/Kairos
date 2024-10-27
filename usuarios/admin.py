from django.contrib import admin
from .models import User  # Asegúrate de que esta línea sea correcta

@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username',)
