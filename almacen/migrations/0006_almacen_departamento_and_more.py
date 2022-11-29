# Generated by Django 4.1.2 on 2022-10-07 15:59

import almacen.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0005_alter_almacen_nombre_alter_articulo_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacen',
            name='departamento',
            field=models.TextField(choices=[('TJ', 'TARIJA'), ('OR', 'ORURO'), ('PT', 'POTOSI'), ('LP', 'LA PAZ'), ('CB', 'COCHABAMBA'), ('SC', 'SANTA CRUZ'), ('CH', 'CHUQUISACA'), ('PD', 'PANDO'), ('BN', 'BENI')], default='TJ', max_length=2),
        ),
        migrations.AddField(
            model_name='articulo_proveedor',
            name='cantidad_enviada',
            field=models.BigIntegerField(default=1, validators=[almacen.validators.validar_cantidad]),
        ),
        migrations.AddField(
            model_name='articulo_proveedor',
            name='cantidad_registrada',
            field=models.BigIntegerField(default=1, validators=[almacen.validators.validar_cantidad]),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='direccion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(default='', max_length=50, validators=[almacen.validators.validar_nombres]),
        ),
    ]
