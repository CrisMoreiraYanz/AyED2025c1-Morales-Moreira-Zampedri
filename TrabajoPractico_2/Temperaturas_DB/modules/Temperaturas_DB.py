
class temperatura:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura
        self.datos = {}  
    
    #guarda la medida de temperatura asociada a la fecha.
    def guardar_temperatura(self, temperatura, fecha): 
        self.datos[fecha]= temperatura

    #devuelve la medida de temperatura en la fecha determinada.
    def devolver_temperatura(self, fecha): 
        return self.datos.get(fecha, None) 
         
    #devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
    #Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
    def max_temp_rango(self, fecha1, fecha2): 
        temps = [t for f, t in self.datos.items() if fecha1 <= f <= fecha2]
        return max(temps) if temps else None

    #devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
    #Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
    def min_temp_rango(self, fecha1, fecha2): 
        temps = [t for f, t in self.datos.items() if fecha1 <= f <= fecha2]
        return min(temps) if temps else None

    #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
    def temp_extremos_rango(self, fecha1, fecha2):
        temps = [t for f, t in self.datos.items() if fecha1 <= f <= fecha2]
        if temps:
            return min(temps), max(temps)
        return None, None

    #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
    def borrar_temperatura(self, fecha): 
        if fecha in self.datos:
            del self.datos[fecha]

    #devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas.
    def devolver_temperaturas(self, fecha1, fecha2):  
        result = []
        for f in sorted(self.datos):
            if fecha1 <= f <= fecha2:
                result.append(f"{f}: {self.datos[f]} ºC")
        return result

    #devuelve la cantidad de muestras de la BD.
    def cantidad_muestras(self): 
        return len(self.datos)

# if __name__ == "__main__":
#     # Ejemplo de uso
#     t = temperatura("01/01/2023", 25)
#     t.guardar_temperatura(30, "02/01/2023")
#     t.guardar_temperatura(20, "03/01/2023")
#     print("temperatura el dia 1 al 3",t.devolver_temperaturas("01/01/2023", "03/01/2023"))
#     print("maximo de temperatura entre el uno y el 3",t.max_temp_rango("01/01/2023", "03/01/2023"))
#     print("minimo de temperatura entre el uno y el 3",t.min_temp_rango("01/01/2023", "03/01/2023"))
#     print("nose",t.temp_extremos_rango("01/01/2023", "03/01/2023"))
#     t.borrar_temperatura("02/01/2023")
#     print("devuelve temperatura despues de borrar",t.devolver_temperaturas("01/01/2023", "03/01/2023"))



    