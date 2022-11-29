from django.core.exceptions import ValidationError

def validar_nombre_categoria(value):
    if value == '':
        raise ValidationError('Categoria no valida')
def validar_proveedor(value):
    if value == '':
        raise ValidationError('Proveedor no valido')
def validar_cantidad_articulo_almacen(value):
    if value==0:
        raise ValidationError('Debe ingresar al menos una unidad')
def validar_nombres(value):
    if value == '':
        raise ValidationError('Debe ingresar un nombre correcto')
def validar_cantidad(value):
    if value==0:
        raise ValidationError('Debe ingresar al menos una unidad')