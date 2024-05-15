# 1

VOCALES = 'aeiou'

def conjuntos_string(conjunto,caracter) -> bool:

    flag = False
    for i in range(len(conjunto)):
        if conjunto[i] == caracter:
            flag = True
            break
    return flag


def cantidad_vocales(cadena,vocal) -> int | None:
    flag = conjuntos_string(VOCALES, vocal)
    vocal = vocal

    if flag:
        contador = 0
        for i in range(len(cadena)):
            if cadena[i] == vocal:
                contador += 1
        
        return contador


def matriz_interfas(cadena):
    for i in range(len(VOCALES)):
            cantidad = cantidad_vocales(cadena,VOCALES[i])
            cantidad = str(cantidad)
            print(f'{VOCALES[i]} -> {cantidad}', end= '\n')

print(matriz_interfas('lalolandalila'))