from sys import maxsize
from modulos.cola_prioridad import ColaDePrioridad
from modulos.grafo import Grafo
# Algoritmo de Prim para encontrar el árbol de expansión mínima en un grafo ponderado
def prim(G,inicio):
    cp=ColaDePrioridad()
    # Se sobrecarga __iter__ para que funcione con el montículo
    for v in G:
        # Se asigna una distancia infinita a todos los vértices excepto al inicial
        v.asignar_distancia(maxsize)
        # Se asigna un predecesor nulo a todos los vértices
        v.asignar_predecesor(None)
    # Se asigna una distancia de 0 al vértice inicial    
    inicio.asignar_distancia(0)
    # Se construye la cola de prioridad con los vértices del grafo
    cp.construir_monticulo([(v.obtener_distancia(),v) for v in G])    

    # Se pregunta si la cola de prioridad esta vacia
    # Mientras la cola de prioridad no este vacia, se extrae el vértice con la menor distancia
    while not cp.esta_vacia():
        # Se extrae elemento 1 de la tupla (distancia, vertice)
        vertice_actual = cp.desencolar()[1]
        # Se itera sobre todas las conexiones del vertice actual
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            nuevo_costo=vertice_actual.obtener_ponderacion(vertice_siguiente)
            # Se pregunta si el vertice siguiente esta en la cola de prioridad y si el nuevo costo es menor que la distancia actual del vertice siguiente
            # Si es asi, se actualiza la distancia y el predecesor del vertice siguiente
            if cp.contiene(vertice_siguiente) and nuevo_costo < vertice_siguiente.obtener_distancia():
                vertice_siguiente.asignar_distancia(nuevo_costo)
                vertice_siguiente.asignar_predecesor(vertice_actual)
                # Se actualiza la distancia del vertice siguiente en la cola de prioridad
                cp.decrementar_clave(vertice_siguiente,nuevo_costo)

if __name__ == "__main__":
    G = Grafo()
    G.agregar_arista('A', 'B', 4)
    G.agregar_arista('A', 'C', 3)
    G.agregar_arista('B', 'C', 1)
    G.agregar_arista('B', 'D', 2)
    G.agregar_arista('C', 'D', 4)
    G.agregar_arista('D', 'E', 2)

    inicio = G.obtener_vertice('A')
    prim(G, inicio)
    print ("Árbol de expansión mínima:")
    for v in G:
        if v.predecesor:
            print(f"{v.predecesor.id} -> {v.id} (Peso: {v.obtener_ponderacion(v.predecesor)})")
        else:
            print(f"{v.id} (Inicio)")  # Vertice inicial sin predecesor
