# archivo: modulos/cola_prioridad.py
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

    def __iter__(self):
        return iter(self._monticulo)
