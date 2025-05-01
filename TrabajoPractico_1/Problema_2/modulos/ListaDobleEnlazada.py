class Nodo:
    """Clase Nodo para la Lista Doble Enlazada"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    """Implementación del TAD Lista Doble Enlazada"""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def __len__(self):
        return self.tamanio

    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")
        if posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion == self.tamanio:
            self.agregar_al_final(item)
        else:
            nuevo_nodo = Nodo(item)
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            nuevo_nodo.siguiente = nodo_actual
            nuevo_nodo.anterior = nodo_actual.anterior
            nodo_actual.anterior.siguiente = nuevo_nodo
            nodo_actual.anterior = nuevo_nodo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("No se puede extraer de una lista vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0:  
            posicion += self.tamanio
        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")
        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente
            dato = nodo_actual.dato
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior
        self.tamanio -= 1
        return dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual:
            copia.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        if copia.cabeza:
            copia.cabeza.anterior=None
        return copia

    def invertir(self):
        nodo_actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza
        while nodo_actual is not None:
            nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior, nodo_actual.siguiente
            nodo_actual = nodo_actual.anterior
        return self
    
    def concatenar(self, otra_lista):
        if otra_lista.esta_vacia(): 
            return self
        if self.esta_vacia():
            return otra_lista
        else:
            self.cola.siguiente = otra_lista.cabeza
            # otra_lista.cabeza.anterior = self.cola
            self.cola = otra_lista.cola
            self.tamanio += len(otra_lista)
            return self

    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista

    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente

    def __str__(self):
        """Devuelve una representación en cadena de la lista."""
        elementos = []
        nodo_actual = self.cabeza
        while nodo_actual:
            elementos.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.siguiente
        return " <-> ".join(elementos)
    
if __name__ == "__main__":
    lista1=ListaDobleEnlazada()
    lista2=ListaDobleEnlazada()
    for i in range(30):
        lista1.agregar_al_final(i)
        lista2.agregar_al_final(i+20)
        
    # for i in lista1:
    #     print(i, end=" ")
    lista3=ListaDobleEnlazada()
    lista3=lista1.concatenar(lista2)
    print("tamaño lista", len(lista3))
    for i in lista3:
        print(i, end=" ")
    # print(lista1.invertir())

   
    
