#Ordenamiento Burbuja
def bubble_sort (lista):
    for pasar_numero in range (len(lista)-1,0,-1):
        for i in range(pasar_numero):
            if lista[i] > lista[i+1]:
                temp= lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp

#Ordenamiento Quicksort
def quick_sort (lista):
    quick_sort_helper(lista,0,len(lista)-1)

def quick_sort_helper(lista,primero,ultimo):
    if primero<ultimo:
        punto_particion=particion(lista,primero,ultimo)
        

    