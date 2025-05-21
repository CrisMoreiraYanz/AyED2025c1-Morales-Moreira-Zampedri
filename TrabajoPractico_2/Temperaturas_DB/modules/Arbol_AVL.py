from modules.nodo import NodoArbol
class AVLTree:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        if not self.raiz:
            self.raiz = NodoArbol(clave, valor)
        else:
            self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            return NodoArbol(clave, valor)

        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._insertar(nodo.hijoIzquierdo, clave, valor)
            nodo.hijoIzquierdo.padre = nodo
        else:
            nodo.hijoDerecho = self._insertar(nodo.hijoDerecho, clave, valor)
            nodo.hijoDerecho.padre = nodo

        nodo.factorEquilibrio = self._calcularFactorEquilibrio(nodo)
        return self._balancear(nodo)

    def _calcularFactorEquilibrio(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.hijoIzquierdo) - self._altura(nodo.hijoDerecho)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.hijoIzquierdo), self._altura(nodo.hijoDerecho))

    def _balancear(self, nodo):
        if nodo.factorEquilibrio > 1:
            if nodo.hijoIzquierdo and nodo.hijoIzquierdo.factorEquilibrio < 0:
                nodo.hijoIzquierdo = self._rotarIzquierda(nodo.hijoIzquierdo)
            return self._rotarDerecha(nodo)

        if nodo.factorEquilibrio < -1:
            if nodo.hijoDerecho and nodo.hijoDerecho.factorEquilibrio > 0:
                nodo.hijoDerecho = self._rotarDerecha(nodo.hijoDerecho)
            return self._rotarIzquierda(nodo)

        return nodo

    def _rotarDerecha(self, nodo):
        nuevoRaiz = nodo.hijoIzquierdo
        nodo.hijoIzquierdo = nuevoRaiz.hijoDerecho
        nuevoRaiz.hijoDerecho = nodo
        nodo.factorEquilibrio = self._calcularFactorEquilibrio(nodo)
        nuevoRaiz.factorEquilibrio = self._calcularFactorEquilibrio(nuevoRaiz)
        return nuevoRaiz

    def _rotarIzquierda(self, nodo):
        nuevoRaiz = nodo.hijoDerecho
        nodo.hijoDerecho = nuevoRaiz.hijoIzquierdo
        nuevoRaiz.hijoIzquierdo = nodo
        nodo.factorEquilibrio = self._calcularFactorEquilibrio(nodo)
        nuevoRaiz.factorEquilibrio = self._calcularFactorEquilibrio(nuevoRaiz)
        return nuevoRaiz

    def eliminar(self, clave):
        if self.raiz:
            self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return nodo

        if clave < nodo.clave:
            nodo.hijoIzquierdo = self._eliminar(nodo.hijoIzquierdo, clave)
        elif clave > nodo.clave:
            nodo.hijoDerecho = self._eliminar(nodo.hijoDerecho, clave)
        else:
            if nodo.tieneHijoIzquierdo() and nodo.tieneHijoDerecho():
                sucesor = self._encontrarMinimo(nodo.hijoDerecho)
                nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
                nodo.hijoDerecho = self._eliminar(nodo.hijoDerecho, sucesor.clave)
            else:
                nodo = nodo.hijoIzquierdo if nodo.tieneHijoIzquierdo() else nodo.hijoDerecho

        if nodo is None:
            return nodo

        nodo.factorEquilibrio = self._calcularFactorEquilibrio(nodo)
        return self._balancear(nodo)

    def _encontrarMinimo(self, nodo):
        while nodo.hijoIzquierdo is not None:
            nodo = nodo.hijoIzquierdo
        return nodo

    def inorden(self):
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        return self._inorden(nodo.hijoIzquierdo) + [(nodo.clave, nodo.valor)] + self._inorden(nodo.hijoDerecho) if nodo else []

if __name__=="__main__":
    arbol = AVLTree()
    arbol.insertar(10, "A")
    arbol.insertar(20, "B")
    arbol.insertar(30, "C")
    arbol.insertar(40, "D")
    arbol.insertar(50, "E")
    arbol.insertar(25, "F")

    print("Inorden:", arbol.inorden())
    arbol.eliminar(30)
    print("Inorden después de eliminar 30:", arbol.inorden()) 





