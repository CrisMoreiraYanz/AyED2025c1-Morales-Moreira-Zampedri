from modulos.mont_binario import monticulobinario

class ColaDePrioridad:
    def __init__(self):
        self._monticulo = monticulobinario()

    def encolar(self, elemento):
        self._monticulo.insertar(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("Cola vacía")
        return self._monticulo.extraer_minimo()

    def esta_vacia(self):
        return self._monticulo.tamanio_monticulo() == 0

    def tamanio(self):
        return self._monticulo.tamanio_monticulo()
    
    def construir_monticulo(self, lista):
        self._monticulo.construir_monticulo(lista)

    def decrementar_clave(self, vertice, nuevo_valor):
        for i in range(1, self._monticulo.tamanio_monticulo() + 1):
            if self._monticulo.lista_monticulo[i][1] == vertice:
                self._monticulo.lista_monticulo[i] = (nuevo_valor, vertice)
                self._monticulo.infiltrar_arriba(i)
                break    

    def contiene(self, vertice):
        for i in range(1, self._monticulo.tamanio_monticulo() + 1):
            if self._monticulo.lista_monticulo[i][1] == vertice:
                return True
        return False

    def __iter__(self):
        return iter(self._monticulo)
