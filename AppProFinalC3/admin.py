from django.contrib import admin
from .models import Producto
from .models import Proveedor
from .models import Barra
from .models import Venta

# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Barra)
admin.site.register(Venta)
