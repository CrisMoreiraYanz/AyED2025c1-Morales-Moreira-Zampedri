#Ordenamiento Burbuja
def bubble_sort (lista):
    for pasar_numero in range (len(lista)-1,0,-1):
        for i in range(pasar_numero):
            if lista[i] > lista[i+1]:
                temp= lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp


        

    