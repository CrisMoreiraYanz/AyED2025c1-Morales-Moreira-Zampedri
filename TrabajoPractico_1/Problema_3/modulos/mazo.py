#algoritmo clase mazo
class Mazo:
    def __init__(self, cartas):
        self.cartas = cartas

    def mezclar(self):
        import random
        random.shuffle(self.cartas)

    def repartir(self, num_cartas):
        return [self.cartas.pop() for _ in range(num_cartas)] if len(self.cartas) >= num_cartas else None

    def __str__(self):
        return f"Mazo con {len(self.cartas)} cartas."