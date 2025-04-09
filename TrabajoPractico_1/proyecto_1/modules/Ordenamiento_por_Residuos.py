#Ordenamiento por residuos/radix sort
def radix_sort(lista_sin_ordenar):
    valor_maximo = max(lista_sin_ordenar)
    exponente_maximo = len(str(valor_maximo)) 
    ordenado = lista_sin_ordenar[:]
    for exponente in range(max_exponent):
        posicion = exponente + 1
        index = - posicion
        x = [[] for i in range(10)]
        for numero in ordenado:
            numero_cadena = str(numero)
            try:
                digito = numero_cadena[index]
                except IndexError: 
                digito = 0
                digito = int(digito)
                x[digito].append(numero)
        ordenado = []
        for numeral in x:
            ordenado.extend(numeral)       

