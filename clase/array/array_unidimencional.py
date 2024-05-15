# 1_Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.


def calcular_pormedio(lista:list)-> None:
    acumulador = 0
    for num  in range(len(lista)):
        acumulador += lista[num]

    promedio = acumulador / len(lista)

    return promedio


# 2_Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
 
def calcular_pormedio_positivo(lista:list)-> None:
    acumulador_positivo = 0
    acumulador = 0

    for num  in range(len(lista)):

        if lista[num] > 0:

            acumulador_positivo += 1
            acumulador += lista[num]


    promedio = acumulador / acumulador_positivo

    return promedio


def cantidad_positivo(lista):
    acumulador_positivo = 0

    for num  in range(len(lista)):

        if lista[num] > 0:

            acumulador_positivo += 1
    return acumulador_positivo


# 3_Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.


def producto_de_una_lista(lista):
    total = 1
    for i in range(len(lista)):
        total *= i 

    return total

# 4_Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado
def encontrar_maximo_indice(lista:list):
    maximo = None
    for i in range(len(lista)):
        if maximo == None or maximo < lista[i] :
            maximo = i

    return maximo


# print(encontrar_maximo_indice([3,5,6,4,3,100,4,3,5,100]))

    
# 5_Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def encontrar_los_mayores_valores(lista):
    acumulador_de_valores_maximo = 1
    maximo_valor = encontrar_maximo_indice(lista)
    for i in range(len(lista)):
        if lista[i] == lista[maximo_valor] and i != maximo_valor:
            acumulador_de_valores_maximo += 1
    indice_valores_maximo = [0] * acumulador_de_valores_maximo
        
    for i in range(len(indice_valores_maximo)):
        for j in range(len(lista)):
            if lista[j] == lista[maximo_valor] and j != i:
                indice_valores_maximo[i] = j 
                
    return indice_valores_maximo
print(encontrar_los_mayores_valores([3,5,6,4,3,100,4,3,5,100]))

# 6_Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.



def reemplazar_nombres(lista,nombre,update):
    reemplazos = 0
    for i in range(len(lista)):
        if lista[i] == nombre:
            reemplazos += 1
            lista[i] == update
    return reemplazos