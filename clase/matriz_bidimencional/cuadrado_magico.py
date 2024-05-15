n = input('elija una matriz de n x n ')
n = int(n)
matriz = [[0]*n for _ in range(n)]

M = len(matriz)
N = len(matriz[0])
NM = N * (N**2 + 1) / 2


def recorrer_matriz(matriz):
    for columna in range(M):
        for fila in range(N):
            numero = int(input('ingrese un numero: '))
            parse_num = numero
            matriz[columna][fila] = parse_num




def suma_columna(matriz,columna):
    total = 0
    for i in range(M):
        total += matriz[i][columna]
        print(f'{matriz[i][columna]} ',end='')
    return total


def recorrer_columna(matriz):
    for i in range(N):
        a = suma_columna(matriz,i)
        if a != NM:
            return True

# recorrer_columna(matriz)
        
def recorrer_diagonal(matriz):
    diagonal = 0
    suma = 0
    for fila in range(M):
        # print(matriz[fila][diagonal])
        suma += matriz[fila][diagonal]
        diagonal += 1
    return suma
        
def recorrer_diagonal_contraria(matriz):
    diagonal = N - 1
    suma = 0
    for fila in range(M):
        # print(matriz[fila][diagonal])
        suma += matriz[fila][diagonal]
        diagonal -= 1
    return suma

def diagonales(matriz):
    diagonal = recorrer_diagonal(matriz)
    diagonal_contraria = recorrer_diagonal_contraria(matriz)
    if diagonal != NM or diagonal_contraria != NM:
        return True 



# ------------------- validaciones --------------------------------
def get_int(num:int , mensaje_error:str, minimo:int, maximo:int, reintento: int)-> int|None:
    'obtiene un numero entero'
    validate = validacion_int(num, minimo, maximo, reintento, mensaje_error)
    if validate:
            parse_int = num
            return parse_int

     

def validacion_int(num:int, minimo:int, maximo:int, reintento:int, mesaje_error) -> bool|None:
    '''valida si el numero es entero segun los parametros dados
    parametros: minimo, maximo, reintentos'''

    parse_int = num
    validacion = True
    contador = 0
    
    while type(parse_int) == str or parse_int < minimo or parse_int > maximo :
        
        contador += 1
        num = input('ingrese un numero entre los rangos: ')
        parse_int = int(num)

        if contador == reintento:
            print('{}'.mesaje_error)
            validacion = False

    return validacion
        
    

# ------------------- cuadrado magico --------------------------------
while True:
    recorrer_matriz(matriz)
    # matriz = [[8,1,6],[3,5,7],[4,9,2]]
    cuadrado_magico = True
    if recorrer_columna(matriz) == True:
        cuadrado_magico = False
        
    if diagonales(matriz) == True:
       cuadrado_magico = False


    if cuadrado_magico == True:
        print ('tenes un cuadrado magico ')
        break
    else:
        print('no es un cuadrado magico ')

