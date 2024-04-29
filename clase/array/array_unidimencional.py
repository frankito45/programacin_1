# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.


def calcular_pormedio(lista:list)-> None:
    acumulador = 0
    for num  in range(len(lista)):
        acumulador += lista[num]

    promedio = acumulador / len(lista)

    return promedio


# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
 
def calcular_pormedio_positivo(lista:list)-> None:
    acumulador_positivo = 0
    acumulador = 0

    for num  in range(len(lista)):

        if lista[num] > 0:

            acumulador_positivo += 1
            acumulador += lista[num]


    promedio = acumulador / acumulador_positivo

    return promedio


# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado
def encontrar_maximo_indice(lista:list) -> None:
    maximo = None
    for i in range(len(list)):
        if maximo < i or maximo == None:
            maximo = i


def cantidad_positivo(lista):
    acumulador_positivo = 0

    for num  in range(len(lista)):

        if lista[num] > 0:

            acumulador_positivo += 1
    return acumulador_positivo

    
print(len([4,-44,-4,-4,4])-cantidad_positivo([4,-44,-4,-4,4]))