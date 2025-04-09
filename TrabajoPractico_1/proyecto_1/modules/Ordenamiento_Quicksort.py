#Ordenamiento Quicksort
def quick_sort (lista):
    quick_sort_helper(lista,0,len(lista)-1)

def quick_sort_helper(lista,primero,ultimo):
    if primero<ultimo:
        punto_particion=particion(lista,primero,ultimo)
        