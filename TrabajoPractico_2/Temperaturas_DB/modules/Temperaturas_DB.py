from modules.Arbol_AVL import AVLTree

class Temperatura:
    def __init__(self):
        self.fecha = None
        self.temperatura = None
        self.arbol = AVLTree()  
    
    #guarda la medida de temperatura asociada a la fecha.
    def guardar_temperatura(self, temperatura, fecha): 
        # self.arbol[fecha] = temperatura
        self.arbol.insertar(fecha, temperatura)

    #devuelve la medida de temperatura en la fecha determinada.
    def devolver_temperatura(self, fecha): 
        return self.arbol.buscar(fecha, None) 

    def temperaturas_en_rango(self, fecha1, fecha2):
        temperaturas = self.arbol.inorden()
        return [temperatura for fecha, temperatura in temperaturas if fecha1 <= fecha <= fecha2]  
       
    #devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
    #Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
    def max_temp_rango(self, fecha1, fecha2): 
        temperaturas = self.temperaturas_en_rango(fecha1, fecha2)
        return max(temperaturas) if temperaturas else None
    
    #devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
    #Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
    def min_temp_rango(self, fecha1, fecha2): 
        temperaturas = self.temperaturas_en_rango(fecha1, fecha2)
        return min(temperaturas) if temperaturas else None

    #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
    def temp_extremos_rango(self, fecha1, fecha2):
        temperaturas = self.temperaturas_en_rango(fecha1, fecha2)
        if temperaturas:
            return min(temperaturas), max(temperaturas)
        return None, None

    #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
    def borrar_temperatura(self, fecha): 
       self.arbol.eliminar(fecha)

    #devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas.
    def devolver_temperaturas(self, fecha1, fecha2):  
        temperaturas = self.arbol.inorden()
        rango_temperaturas = []
        for fecha, temperatura in temperaturas:
            if fecha1 <= fecha <= fecha2:
                rango_temperaturas.append(f"{fecha}: {temperatura} ºC")
        return rango_temperaturas

    #devuelve la cantidad de muestras de la BD.
    def cantidad_muestras(self): 
        return len(self.arbol.inorden())
    
    def devolver_raiz(self):
        return self.arbol.devolver_raiz()
    
    def __str__(self):
        temperaturas = self.arbol.inorden()
        return (2*"\n ").join([f"{fecha}: {temperatura} ºC" for fecha, temperatura in temperaturas])

if __name__ == "__main__":
        temp_db = Temperatura()
        temp_db.guardar_temperatura(25, "01/01/2023")
        temp_db.guardar_temperatura(30, "02/01/2023")
        temp_db.guardar_temperatura(20, "03/01/2023")
        temp_db.guardar_temperatura(15, "04/01/2023")
        temp_db.guardar_temperatura(35, "05/01/2023")
        temp_db.guardar_temperatura(28, "06/01/2023")
        temp_db.guardar_temperatura(22, "07/01/2023")
        print("\nTemperaturas del 01/01/2023 al 03/01/2023:",temp_db.devolver_temperaturas("01/01/2023", "07/01/2023"))
        print("\nTemperatura del 02/01/2023:",temp_db.devolver_temperatura("02/01/2023"))
        print("\nTemperatura mínima:",temp_db.min_temp_rango("01/01/2023", "07/01/2023"))
        print("\nTemperatura máxima:",temp_db.max_temp_rango("01/01/2023", "07/01/2023"))
        print("\nValores extremos de temperatura:",temp_db.temp_extremos_rango("01/01/2023", "07/01/2023"))
        temp_db.borrar_temperatura("02/01/2023")
        print("\nCantidad de muestras tomadas:",temp_db.cantidad_muestras())
        temp_db.guardar_temperatura(30, "02/01/2023")
        print("\nRaiz del arbol:",temp_db.devolver_raiz())
        temp_db.borrar_temperatura("05/01/2023")
        print("\nÁrbol después de boorrar 05/01/2023:\n",temp_db)    
        temp_db.borrar_temperatura("04/01/2023")
        print("\nÁrbol después de borrar 04/01/2023:\n", temp_db)
        temp_db.guardar_temperatura(25, "05/01/2023")
        print("\nÁrbol después de volver a insertar 05/01/2023:\n", temp_db)
        print("\nRaiz del arbol:",temp_db.devolver_raiz())
        
       