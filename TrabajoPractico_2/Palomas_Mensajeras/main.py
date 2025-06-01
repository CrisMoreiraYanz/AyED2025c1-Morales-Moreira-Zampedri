from modulos.grafo import Grafo
from modulos.prim import prim
from modulos.exportar import ExportarGraphviz
def cargar_grafo(nombre_archivo):
    G = Grafo()
    with open("data/aldeas.txt") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                origen = partes[0].strip()
                destino = partes[1].strip()
                peso = int(partes[2].strip())
                G.agregar_arista(origen, destino, peso)
            elif len(partes) == 1:
                # Por si hay una aldea aislada sin conexiones
                G.agregar_vertice(partes[0].strip())
    return G

grafo = cargar_grafo("aldeas.txt")
inicio = grafo.obtener_vertice("Peligros")
prim(grafo, inicio)          

if __name__ == "__main__":
    #Mostrar aldeas en orden alfabético
    print("Lista de aldeas en orden alfabético:")
    for v in sorted(grafo, key=lambda x: x.id):
       print(v.id)
    replicas = {v.id: [] for v in grafo}


    #Para cada aldea, mostrar de qué vecina debería recibir la noticia, 
    #y a qué vecinas debería enviar réplicas
    for v in grafo:
        if v.predecesor:
            padre = v.predecesor.id
            replicas[padre].append(v.id)

    print("\nRutas óptimas de mensajes (desde Peligros):\n")
    for v in sorted(grafo, key=lambda x: x.id):
        if v.predecesor:
            print(f"{v.id} debe recibir el mensaje desde {v.predecesor.id}")
        else:
            print(f"{v.id} (Inicio - envía mensajes)")
        if replicas[v.id]:
            print(f"  → Y debe reenviar a: {', '.join(sorted(replicas[v.id]))}") 

    #Mostrar la suma total de distancias recorridas
    suma_total = 0
    for v in grafo:
        if v.predecesor:
            suma_total += v.obtener_ponderacion(v.predecesor)

    print(f"\nDistancia total recorrida por todas las palomas: {suma_total} leguas")    

    #Exportar el grafo a Graphviz para verificar el árbol de expansión mínima
    ExportarGraphviz(grafo, "mst.dot")      