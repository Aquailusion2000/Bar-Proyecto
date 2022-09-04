from dataclasses import fields
from rest_framework import serializers
from .models import Producto
from .models import Proveedor
from .models import Barra
from .models import Venta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_Producto', 'nombre_producto', 'tipo_producto', 'cantidad_producto', 
                  'existencia_producto','fecha_vencimiento', 'proveedor']
    
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id_Proveedor', 'nombre', 'localizacion', 'suministro', 'condicion_pago', 'forma_contacto']

class BarraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barra
        fields = ['id_producto_barra', 'valor_licor', 'valor_aco', 'producto']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id_venta', 'producto_barra', 'cantidad', 'fecha_venta']


