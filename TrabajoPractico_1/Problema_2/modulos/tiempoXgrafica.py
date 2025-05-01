from modulos.ListaDobleEnlazada import ListaDobleEnlazada  
import time
import matplotlib.pyplot as plt

def medir_tiempos(lista, tamaños):
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for n in tamaños:
        # Agregar elementos a la lista
        for i in range(n):
            lista.agregar_al_final(i)

        # Medir tiempo de len
        inicio = time.time()
        len(lista)
        tiempos_len.append(time.time() - inicio)

        # Medir tiempo de copiar
        inicio = time.time()
        lista.copiar()
        tiempos_copiar.append(time.time() - inicio)

        # Medir tiempo de invertir
        inicio = time.time()
        lista.invertir()
        tiempos_invertir.append(time.time() - inicio)

        # Limpiar la lista para la próxima iteración
        lista.extraer(posicion=0)  # Extraer el primer elemento hasta que quede vacía
        for _ in range(n-1):
            lista.extraer(posicion=0)

    return tiempos_len, tiempos_copiar, tiempos_invertir

# Crear lista y tamaños
lista = ListaDobleEnlazada()
tamaños = [10, 100, 1000, 5000, 10000]

# Medir tiempos
tiempos_len, tiempos_copiar, tiempos_invertir = medir_tiempos(lista, tamaños)

# Graficar resultados
plt.figure(figsize=(10, 5))
plt.plot(tamaños, tiempos_len, label='len', marker='o')
plt.plot(tamaños, tiempos_copiar, label='copiar', marker='o')
plt.plot(tamaños, tiempos_invertir, label='invertir', marker='o')
plt.xlabel('Cantidad de elementos (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('N vs Tiempo de Ejecución')
plt.legend()
plt.grid()
plt.show()