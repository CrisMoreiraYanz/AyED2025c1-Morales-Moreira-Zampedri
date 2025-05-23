class monticulobinario:
    def __init__(self):
        self.lista_monticulo = [None]
        self.tamanio = 0

    def tamanio_monticulo(self):
        return self.tamanio

    def infiltrar_arriba(self,valor):
        while valor//2 > 0:
          if self.lista_monticulo[valor] < self.lista_monticulo[valor//2]:
            tmp=self.lista_monticulo[valor//2]
            self.lista_monticulo[valor//2]=self.lista_monticulo[valor]
            self.lista_monticulo[valor]=tmp
          valor=valor//2

    def insertar(self,valor):
      self.lista_monticulo.append(valor)
      self.tamanio+=1
      self.infiltrar_arriba(self.tamanio)     

    def hijo_min(self, valor):
        if valor * 2 + 1 > self.tamanio:
          return valor * 2
        else:
          if self.lista_monticulo[valor * 2] < self.lista_monticulo[valor * 2 + 1]:
             return valor * 2
          else:
             return valor * 2 + 1
        
    def infiltrar_abajo(self,valor):
      while (valor * 2) <= self.tamanio:
         hm = self.hijo_min(valor)
         if self.lista_monticulo[valor] > self.lista_monticulo[hm]:
               tmp = self.lista_monticulo[valor]
               self.lista_monticulo[valor] = self.lista_monticulo[hm]
               self.lista_monticulo[hm] = tmp
         valor = hm      

    def extraer_minimo(self):
       ret_val = self.lista_monticulo[1]
       self.lista_monticulo[1] = self.lista_monticulo[self.tamanio]
       self.tamanio = self.tamanio - 1
       self.lista_monticulo.pop()
       self.infiltrar_abajo(1)
       return ret_val

    def construir_monticulo(self,lista):
       i = len(lista) // 2
       self.tamanio = len(lista)
       self.lista_monticulo = [0] + lista[:]
       while (i > 0):
         self.infiltrar_abajo(i)
         i -= 1   
         
    def __iter__(self):
         for i in range(1, self.tamanio + 1):
              yield self.lista_monticulo[i]   
        

if __name__== "__main__":
   monticulo = monticulobinario()
   lista = [5, 3, 8, 1, 4, 7, 2, 6]
   monticulo.construir_monticulo(lista)
   print("Montículo binario construido:", monticulo.lista_monticulo[1:])
    
   monticulo.insertar(0)
   print("Después de insertar 0:", monticulo.lista_monticulo[1:])
    
   min_val = monticulo.extraer_minimo()
   print("Valor mínimo extraído:", min_val)
   print("Después de extraer el mínimo:", monticulo.lista_monticulo[1:])

   print ("Fin del programa")