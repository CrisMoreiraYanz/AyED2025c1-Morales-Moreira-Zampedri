import unittest
from proyecto_1.Ordenamiento_Burbuja import burbuja

class TestOrdenamientoBurbuja(unittest.TestCase):
    def test_lista_ordenada(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(burbuja(lista), [1, 2, 3, 4, 5])

    # def test_lista_desordenada(self):
    #     lista = [5, 3, 1, 4, 2]
    #     self.assertEqual(burbuja(lista), [1, 2, 3, 4, 5])

    # def test_lista_vacia(self):
    #     lista = []
    #     self.assertEqual(burbuja(lista), [])

    # def test_lista_un_elemento(self):
    #     lista = [42]
    #     self.assertEqual(burbuja(lista), [42])

    # def test_lista_elementos_repetidos(self):
    #     lista = [4, 2, 4, 3, 2]
    #     self.assertEqual(burbuja(lista), [2, 2, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()