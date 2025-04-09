#Ordenamiento Quicksort
def quick_sort (lista):
    quick_sort_helper(lista,0,len(lista)-1)
    return lista

def quick_sort_helper(lista,primero,ultimo):
    if primero<ultimo:
        punto_particion=particion(lista,primero,ultimo)
        quick_sort_helper(lista,primero,punto_particion-1)
        quick_sort_helper(lista,punto_particion+1,ultimo)
def particion(lista,primero,ultimo):
    pivote=lista[primero]
    izquierda=primero+1
    derecha=ultimo
    ordenado=False
    while not ordenado:
        while izquierda<=derecha and lista[izquierda]<=pivote:
            izquierda+=1
        while lista[derecha]>=pivote and derecha>=izquierda:
            derecha-=1
        if derecha<izquierda:
            ordenado=True        
        else:
            temp=lista[izquierda]
            lista[izquierda]=lista[derecha]
            lista[derecha]=temp
    lista[primero], lista[derecha] = lista[derecha], lista[primero]        
    return derecha
if __name__ == "__main__":
    l=list(range(10,0,-1))

    lo= quick_sort(l)

    print(lo)        
    
