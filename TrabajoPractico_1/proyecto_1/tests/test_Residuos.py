import unittest
from random import randint
from modules.Ordenamiento_por_Residuos import ordenar_por_residuos

class TestOrdenamientoResiduos(unittest.TestCase):
    def setUp(self):
        self.lista1 = [randint(10000, 99999) for _ in range(500)]

    def test_lista_aleatoria_mayores_500(self):
        self.lista_sort = sorted(self.lista1)
        self.lista_residuos = ordenar_por_residuos(self.lista1)
        self.assertEqual(self.lista_sort, self.lista_residuos)

if __name__ == '__main__':
    unittest.main()