class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conexiones = {} 
        self.distancia = float('inf')
        self.predecesor = None

    def agregar_vecino(self, vecino, peso=0):
        self.conexiones[vecino] = peso

    def obtener_conexiones(self):
        return self.conexiones.keys()

    def obtener_ponderacion(self, vecino):
        return self.conexiones[vecino]

    def asignar_distancia(self, valor):
        self.distancia = valor

    def obtener_distancia(self):
        return self.distancia

    def asignar_predecesor(self, vertice):
        self.predecesor = vertice
        
    def __lt__(self, otro):
        return self.distancia < otro.distancia
                