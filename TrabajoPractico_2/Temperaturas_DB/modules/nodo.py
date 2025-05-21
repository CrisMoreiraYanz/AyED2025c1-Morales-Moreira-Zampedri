class NodoArbol:
    def __init__(self, clave, valor, padre=None):
        self.clave = clave
        self.valor = valor
        self.padre = padre
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.hijoDerecho is not None

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self