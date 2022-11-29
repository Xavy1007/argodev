from email.policy import default

from wsgiref.validate import validator
from django.db import models
from .validators import validar_cantidad, validar_nombre_categoria, validar_nombres, validar_proveedor, validar_cantidad_articulo_almacen

class Proveedor(models.Model):
    idproveedor=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50, validators=[validar_proveedor])
    descripcion=models.TextField()
    telefono= models.CharField(max_length=50, validators=[validar_nombres])
    direccion= models.TextField()
    estado=models.BooleanField(default=True)
    freg=models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    idcategoria=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50, validators=[validar_nombre_categoria])
    descripcion=models.TextField()
    estado=models.BooleanField(default=True)
    freg=models.DateTimeField(auto_now=True)
    def __str__(self):
       # return str(str(self.idcategoria)+", "+self.nombre)
         return str(self.idcategoria)
class Articulo(models.Model):
    idarticulo=models.BigAutoField(primary_key=True)
    nombre=models.TextField(validators=[validar_nombres])
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado=models.BooleanField(default=True)
    freg=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.nombre)

class Deptos(models.TextChoices):
    TJ='TJ','TARIJA'
    OR='OR','ORURO'
    PT='PT','POTOSI'
    LP='LP','LA PAZ'
    CB='CB','COCHABAMBA'
    SC='SC','SANTA CRUZ'
    CH='CH','CHUQUISACA'
    PD='PD','PANDO'
    BN='BN','BENI'

class Almacen(models.Model):
    idalmacen=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50, validators=[validar_nombres])
    descripcion=models.TextField()
    departamento=models.TextField(max_length=2, choices=Deptos.choices,default=Deptos.TJ)
    estado=models.BooleanField(default=True)
    freg=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.nombre)

class Articulo_Almacen(models.Model):
    almacen=models.ForeignKey(Almacen, on_delete=models.CASCADE)
    articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now=True)
    cantidad= models.BigIntegerField(default=1, validators=[validar_cantidad_articulo_almacen])
    estado=models.BooleanField(default=True)
    freg=models.DateTimeField(auto_now=True)
            
class Articulo_proveedor(models.Model):
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad_enviada=models.BigIntegerField(default=1,validators=[validar_cantidad])
    cantidad_registrada=models.BigIntegerField(default=1,validators=[validar_cantidad])
    fecha_ingreso=models.DateTimeField(auto_now=True)
    estado=models.BooleanField(default=True)
    freg=models.DateTimeField(auto_now=True)
