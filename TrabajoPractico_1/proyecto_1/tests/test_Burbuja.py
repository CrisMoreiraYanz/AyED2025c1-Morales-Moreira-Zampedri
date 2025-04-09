import unittest
from random import randint
from modules.Ordenamiento_Burbuja import bubble_sort

class TestOrdenamientoBurbuja(unittest.TestCase):
    def setUp(self):
        self.lista1 =  [randint(10000, 99999) for _ in range(500)] 
        
    # def test_lista_ordenada(self):
    #     lista = [1, 2, 3, 4, 5]
    #     self.assertEqual(burbuja(lista), [1, 2, 3, 4, 5])
    
    def test_lista_aleatoria_mayores_500(self):
        self.lista_sort = sorted(self.lista1)
        self.lista_burbuja = bubble_sort(self.lista1)  

        self.assertEqual(self.lista_sort, self.lista_burbuja)


if __name__ == '__main__':
    unittest.main()