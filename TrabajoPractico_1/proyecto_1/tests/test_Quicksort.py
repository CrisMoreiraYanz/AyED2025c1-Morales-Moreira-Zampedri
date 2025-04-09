import unittest
from random import randint
from modules.Ordenamiento_Quicksort import quick_sort

class TestOrdenamientoQuicksort(unittest.TestCase):
    def setUp(self):
        self.lista1 =  [randint(10000, 99999) for _ in range(500)] 
    
    def test_lista_aleatoria_mayores_500(self):
        self.lista_sort = sorted(self.lista1)
        self.lista_quicksort = quick_sort(self.lista1.copy())  
        self.assertEqual(self.lista_sort, self.lista_quicksort)


if __name__ == '__main__':
    unittest.main()