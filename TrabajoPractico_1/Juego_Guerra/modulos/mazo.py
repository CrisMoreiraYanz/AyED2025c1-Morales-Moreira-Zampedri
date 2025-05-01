# algoritmo clase mazo
from modulos.ListaDobleEnlazada import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    """Excepción personalizada para indicar que el mazo está vacío."""
    pass

class Mazo:
    def _init_(self):
        self.cartas = ListaDobleEnlazada()

    def poner_carta_abajo(self, carta):
        self.cartas.agregar_al_final(carta)

    def poner_carta_arriba(self, carta):
        self.cartas.agregar_al_inicio(carta)

    def sacar_carta_abajo(self):
        if self.cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío. No se puede extraer una carta del final.")
        return self.cartas.extraer(-1)

    def sacar_carta_arriba(self, mostrar=False):
        if self.cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío. No se puede extraer una carta del inicio.")
        carta = self.cartas.extraer(0)
        return carta
            

    def _len_(self):
        """Devuelve la cantidad de cartas en el mazo."""
        return len(self.cartas)

    def _str_(self):
        """Devuelve una representación en cadena del mazo."""
        return " -> ".join(str(carta) for carta in self.cartas)

