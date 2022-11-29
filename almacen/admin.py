from django.contrib import admin
from .models import Almacen, Articulo, Articulo_Almacen, Articulo_proveedor, Proveedor
from .models import Categoria
# Register your models here.
#admin.site.register(Articulo)

class ArticuloTotal(admin.ModelAdmin):
    list_display=("idarticulo","nombre","descripcion","categoria","estado","freg") 

admin.site.register(Articulo, ArticuloTotal)
class CategoriaTotal(admin.ModelAdmin):
    list_display=("idcategoria", "nombre", "descripcion")
    ordering=["idcategoria"]
admin.site.register(Categoria, CategoriaTotal)

class ProveedorTotal(admin.ModelAdmin):
    list_display=("idproveedor","nombre","descripcion","estado","freg") 

admin.site.register(Proveedor, ProveedorTotal)
class AlmacenTotal(admin.ModelAdmin):
    list_display=("idalmacen","nombre","descripcion","departamento","estado","freg") 
admin.site.register(Almacen, AlmacenTotal)
class Articulo_almacenTotal(admin.ModelAdmin):
    list_display=("articulo","almacen","estado","freg") 

admin.site.register(Articulo_Almacen, Articulo_almacenTotal)
class Articulo_provedorTotal(admin.ModelAdmin):
    list_display=("articulo","proveedor","estado","freg") 
admin.site.register(Articulo_proveedor, Articulo_provedorTotal)