from .generales import *
        

def cantidad_positivo(lista) -> int:
    'muestra la cantidad de positivo '
    acumulador_positivo = 0

    for num  in range(len(lista)):

        if lista[num] > 0:

            acumulador_positivo += 1
            
    return acumulador_positivo

def total_positovo_negativo(lista):
    positivo = cantidad_positivo(lista)
    negativo = len(lista) - positivo 
    print(f'cantidad de positivo {positivo}')
    print(f'cantidad de nega1tivo {negativo}')
    
def sumar_las_paridades(lista):
    'suma las paridades '
    acumulador = 0
    for i in range(len(lista)):
        par = par_inpar(lista[i])
        if par :
            acumulador += lista[i]

    return acumulador

def mayor_num_impar(lista):
    'encuentra el mayor numero impar'
    maximo = 0

    for i in range(len(lista)):

        if maximo < lista[i] or maximo == 0 and lista[i] % 2 == 0 :
            maximo = lista[i]

    return maximo
    
def mostrar_lista(lista):
    'muestra la lista'
    for i in range(len(lista)):
        print(lista[i])

def mostrar_numeros_pares(lista):
    'muestra los numeros pares'

    for i in range(len(lista)):
        par = par_inpar(lista[i])
        
        if par:
            print(lista[i])



def posiciones_impares(lista):
    'lista los numero de las posiciones impares'
    for i in range(len(lista)):
        inpar = par_inpar(i)
        if inpar == False:
            print(lista[i])