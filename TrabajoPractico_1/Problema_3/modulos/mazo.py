#algoritmo clase mazo
class Mazo:
    def __init__(self, cartas=None):
        if cartas is None:
            cartas = []  
        self.cartas = cartas

    def poner_carta_arriba(self, carta):
        """Coloca una carta en la parte superior del mazo."""
        self.cartas.append(carta)

    def sacar_carta_arriba(self):
        """Saca y devuelve la carta de la parte superior del mazo."""
        if not self.cartas:
            raise IndexError("El mazo está vacío.")
        return self.cartas.pop()

    def poner_carta_abajo(self, carta):
        """Coloca una carta en la parte inferior del mazo."""
        self.cartas.insert(0, carta)