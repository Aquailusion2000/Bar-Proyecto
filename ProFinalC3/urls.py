"""ProFinalC3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppProFinalC3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proveedores/', views.proveedor_list),
    path('proveedores/<int:id_Proveedor>', views.proveedor_detail),
    path('productos/', views.producto_list),
    path('productos/<int:id_Producto>', views.producto_detail),
    path('barras/', views.barra_list),
    path('barras/<int:id_producto_barra>', views.barra_detail),
    path('ventas/', views.venta_list),
    path('ventas/<int:id_venta>', views.venta_detail)

]
