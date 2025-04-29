from matplotlib import pyplot as plt
from modules.tiempos import medir_tiempos
from modules.Ordenamiento_Burbuja import bubble_sort
from modules.Ordenamiento_Quicksort import quick_sort
from modules.Ordenamiento_por_Residuos import ordenar_por_residuos

def graficar_tiempos(lista_metodos_ord):
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

    for metodo_ord in lista_metodos_ord:
        
        tiempos = medir_tiempos(metodo_ord, tamanos)

        # plot es para graficar los tiempos de ordenamiento
        # plot es el método de matplotlib para graficar
        # marker='o' es para poner un punto en cada coordenada
        plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()


if __name__ == '__main__':
    lista_metodos_ord = [bubble_sort, quick_sort, ordenar_por_residuos]
    graficar_tiempos(lista_metodos_ord)
    # graficar_tiempos([bubble_sort, quick_sort, ordenar_por_residuos])