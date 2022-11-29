from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"almacenes",views.AlmacenViewSet)
router.register(r"articulos",views.ArticulosViewSet)
router.register(r"proveedores",views.ProvedoresViewSet)

urlpatterns = [
    path ('', include(router.urls)),
    path ('articuloscategoria/<int:id>', views.articulo_categoria),
     path ('articulosalmacen/<int:id>', views.articulo_almacen)
]