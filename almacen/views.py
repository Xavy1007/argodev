from operator import contains
from telnetlib import STATUS
from urllib import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .serializers import AlmacenSerializer, Articulo_AlmacenSerializer, CategoriaSerializer, ArticuloSerializer, ProveedorSerializer
from .models import Articulo_Almacen, Categoria, Proveedor, Articulo, Almacen
from django.http import HttpResponse, JsonResponse



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    serializer_class= CategoriaSerializer
class ArticulosViewSet(viewsets.ModelViewSet):
    queryset=Articulo.objects.all()
    serializer_class= ArticuloSerializer
class ProvedoresViewSet(viewsets.ModelViewSet):
    queryset=Proveedor.objects.all()
    serializer_class= ProveedorSerializer
class AlmacenViewSet(viewsets.ModelViewSet):
    queryset=Almacen.objects.all()
    serializer_class= AlmacenSerializer

class CategoriaCreateList(generics.CreateAPIView):
    queryset=Categoria.objects.all()
    serializer_class= CategoriaSerializer

@api_view(['GET'])
def Categoria_contador(request):
    """
    Categoria de items en categoria
    """
    try:
        cantidad= Categoria.objects.count()
        return JsonResponse(
            {
            "cantidad":cantidad    
            },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje":str(e)}, status=400)
@api_view(['GET'])
def articulo_categoria(request, id):
    """
    Articulo por categoria
    """
    try:
        articulo=Articulo.objects.filter(categoria__idcategoria=id)
        return JsonResponse(
            ArticuloSerializer(articulo, many=True).data,
            safe=False,
            status=200
        )
    except Exception as e:
        print(e)
        return JsonResponse({
            "mensaje":"error"
        }, status=400
        )
@api_view(['GET'])
def articulo_almacen(request, id):
    """
    Articulo por por almacen
    """
    try:
        articulos=Articulo_Almacen.objects.filter(almacen__idalmacen=id)
        return JsonResponse(
            Articulo_AlmacenSerializer(articulos, many=True).data,
            safe=False,
            status=200
        )
    except Exception as e:
        print(e)
        return JsonResponse({
            "mensaje":"error"
        }, status=400
        )        