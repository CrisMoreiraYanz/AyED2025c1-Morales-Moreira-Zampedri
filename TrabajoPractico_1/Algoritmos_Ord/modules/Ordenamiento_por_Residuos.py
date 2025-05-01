#Ordenamiento por residuos/radix sort
def ordenar_por_residuos(lista):
    maximo = max(lista)
    lugar = 1
    while maximo // lugar > 0:
        grupos = [[] for _ in range(10)]
        for numero in lista:
            digito = (numero // lugar) % 10
            grupos[digito].append(numero)
        lista = []
        for grupo in grupos:
            lista.extend(grupo)
        lugar *= 10
    return lista