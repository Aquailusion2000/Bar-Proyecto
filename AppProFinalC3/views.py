from django.http import JsonResponse
from .models import Producto
from .models import Proveedor
from .models import Barra
from .models import Venta

from .serializers import ProductoSerializer
from .serializers import ProveedorSerializer
from .serializers import VentaSerializer
from .serializers import BarraSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def proveedor_list(request):

    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def proveedor_detail(request, id_Proveedor):

    try:
        proveedores = Proveedor.objects.get(pk=id_Proveedor)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ProveedorSerializer(proveedores)
        return Response(serializer.data)   
    if request.method == 'PUT':
        serializer = ProveedorSerializer(proveedores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
       proveedores.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)

##----------

@api_view(['GET', 'POST'])
def producto_list(request):

    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def producto_detail(request, id_Producto):

    try:
        productos = Producto.objects.get(pk=id_Producto)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ProductoSerializer(productos)
        return Response(serializer.data)   
    if request.method == 'PUT':
        serializer = ProductoSerializer(productos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
       productos.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
    
    ##------------

@api_view(['GET', 'POST'])
def barra_list(request):

    if request.method == 'GET':
        barras = Barra.objects.all()
        serializer = BarraSerializer(barras, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BarraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def barra_detail(request, id_producto_barra):

    try:
        barras = Barra.objects.get(pk=id_producto_barra)
    except Barra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = BarraSerializer(barras)
        return Response(serializer.data)   
    if request.method == 'PUT':
        serializer = BarraSerializer(barras, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
       barras.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)

##-----------

@api_view(['GET', 'POST'])
def venta_list(request):

    if request.method == 'GET':
        ventas = Venta.objects.all()
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def venta_detail(request, id_venta):

    try:
        ventas = Venta.objects.get(pk=id_venta)
    except Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = VentaSerializer(ventas)
        return Response(serializer.data)   
    if request.method == 'PUT':
        serializer = VentaSerializer(ventas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
       ventas.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
    
