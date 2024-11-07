from django.db import models

#----------------------------------------------
# Carlos puso esto
class Solicitud(models.Model):
    TIPOS = [
        ('P', 'Petición'),
        ('R', 'Reclamo'),
        ('Q', 'Queja'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPOS)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.get_tipo_display()}"
#----------------------------------------------

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

# Nuevo modelo para Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    fecha_compra = models.DateField(auto_now_add=True)
    periodo_garantia = models.IntegerField(default=365)
    
    def esta_en_garantia(self):
        from datetime import datetime
        dias_desde_compra = (datetime.now().date() - self.fecha_compra).days
        return dias_desde_compra <= self.periodo_garantia

# Nuevo modelo para Solicitudes de Garantía
class SolicitudGarantia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    problema = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    codigo_seguimiento = models.CharField(max_length=8, unique=True)