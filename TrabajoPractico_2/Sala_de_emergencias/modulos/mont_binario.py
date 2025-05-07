class monticulobinario:
    def __init__(self):
        self.lista_monticulo = []
        self.tamanio = 0
        
    def infiltrar_arriba(self,valor):
        while i//2 > 0:
          if self.lista_monticulo[i] < self.lista_monticulo[i//2]:
            tmp=self.lista_monticulo[i//2]
            self.lista_monticulo[i//2]=self.lista_monticulo[i]
            self.lista_monticulo[i]=tmp
          i=i//2
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
       while (i * 2) <= self.tamanio:
           mc = self.hijo_min(i)
           if self.lista_monticulo[i] > self.lista_monticulo[mc]:
               tmp = self.lista_monticulo[i]
               self.lista_monticulo[i] = self.lista_monticulo[mc]
               self.lista_monticulo[mc] = tmp
       i = mc      

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
            