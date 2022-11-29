from multiprocessing.connection import Client
from urllib import response
from django.test import TestCase
from django.test import Client

from .models import Categoria
from django.core.exceptions import ValidationError
# Create your tests here.
class Test(TestCase):
    def setUp(self):
        self.client=Client()
        Categoria.objects.create(nombre="CAtegoria2")
        Categoria.objects.create(nombre="CAtegoria3")

    def test_grabacion_categorias(self):
        q= Categoria(nombre="")
        q.save()
        self.assertEqual(Categoria.objects.count(),1)
    def test_grabacion(self):
        q=Categoria.objects.create(nombre="a")
        self.assertRaises(ValidationError,q.full_clean)
    def test_grabacion_nopermitido(self):
        with self.assertRaises(ValidationError) as qv:
            q=Categoria.objects.create(nombre="algo")
            q.full_clean();
        mensaje_error=dict(qv.exception)
        self.assertEqual(mensaje_error["nombre"][0],"No es una opcion")
    def test_categoria_filtro(self):
        response=self.client.get('/almacen/categoria')
        self.assertContains(response, "Categoria 1", status_code=200, html=True)