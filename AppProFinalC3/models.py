from tkinter import CASCADE
from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_Proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    localizacion = models.CharField(max_length=150)
    suministro = models.CharField(max_length=150)
    condicion_pago = models.CharField(max_length=50)
    forma_contacto = models.CharField(max_length=100)

class Producto(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    cantidad_producto = models.IntegerField()
    existencia_producto = models.BooleanField()
    fecha_vencimiento = models.DateTimeField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Barra(models.Model):
    id_producto_barra = models.AutoField(primary_key=True)
    valor_licor = models.IntegerField()
    valor_aco = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    producto_barra = models.ForeignKey(Barra, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateTimeField()


