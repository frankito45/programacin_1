from input_package.input import get_int

def sumar_naturales(numero) -> int:

    if numero > 0:
        numero  = numero + sumar_naturales( numero - 1)

    return numero


def calcular_potencia(base: int, exponente: int) -> int:
    #  calcule la potencia de un número:
    if exponente > 1 :
        base *= calcular_potencia(base, exponente -1)
    
    return base


def sumar_digitos(numero: int) -> int:
    # suma los digitos pasado
    if numero < 10:
        numero = sumar_digitos(numero) % 10
    else:
        numero += numero // 10 
        
    return numero
print(sumar_digitos(432))




def calcular_fibonacci(numero:int) -> int:

    'calcula el numero fibonacci'
    parse_num = get_int(numero)
    
    if numero < 0:
        numero = 1

    elif numero == 0:
        numero = 0

    else:
        numero = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
    
    return numero
