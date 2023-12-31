from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.TextField(null=False, max_length=50, verbose_name="Nombre Producto")
    descripcion = models.TextField(null=False, max_length=200, verbose_name="Descripción Producto")
    existencias = models.IntegerField(null=False, verbose_name="Existencias Producto")
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=12, verbose_name="Precio Producto")


