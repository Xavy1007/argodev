from dataclasses import field
from rest_framework import serializers
from .models import Almacen, Articulo, Articulo_Almacen, Articulo_proveedor, Categoria, Proveedor

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = "__all__"
class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = "__all__"        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"
class Articulo_AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo_Almacen
        fields = "__all__"
class Articulo_ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo_proveedor
        fields = "__all__"        