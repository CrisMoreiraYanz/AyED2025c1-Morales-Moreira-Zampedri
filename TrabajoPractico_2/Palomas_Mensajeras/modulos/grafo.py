from modulos.vertice import Vertice
class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, clave):
        if clave not in self.vertices:
            self.vertices[clave] = Vertice(clave)
        return self.vertices[clave]

    def obtener_vertice(self, clave):
        return self.vertices.get(clave)

    def agregar_arista(self, desde, hasta, peso=1):
        if desde not in self.vertices:
            self.agregar_vertice(desde)
        if hasta not in self.vertices:
            self.agregar_vertice(hasta)
        # Para evitar duplicados, si la arista ya existe para no agregarla de vuelta    
        if hasta not in self.vertices[desde].obtener_conexiones():
            self.vertices[desde].agregar_vecino(self.vertices[hasta], peso)
        if desde not in self.vertices[hasta].obtener_conexiones():
            self.vertices[hasta].agregar_vecino(self.vertices[desde], peso)
    

    def __iter__(self):
        return iter(self.vertices.values())     