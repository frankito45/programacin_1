def crear_matriz(filas,columnas) -> list:
    matriz = [[0]*columnas for _ in range(filas)]
    M = len(matriz)
    N = len(matriz[0])
    
    for i in range (M):
        for j in range(N):
            matriz[i][j] = int(input("Ingrese un numero: "))
            
    return matriz



def mostrar_matriz(matriz):
    for i in range (len(matriz)): 
        for j in range(len(matriz[i])): 
            print(f"{matriz[i][j]}", end = " ")
        print("")


def sumar_filas(matriz):
    M = len(matriz)
    N = len(matriz[0])
    CM = N * (N**2 + 1) / 2
    cuadrado_magico = True
    for i in range(M):
        suma_filas = 0
        for j in range(N):
            suma_filas += matriz[i][j]
        if suma_filas != CM:
            cuadrado_magico = False
            break
    return cuadrado_magico

def sumar_columnas(matriz):
    M = len(matriz)
    N = len(matriz[0])
    CM = N * (N**2 + 1) / 2
    cuadrado_magico = True
    for i in range(M):
        suma_columnas = 0
        for j in range(N):
            suma_columnas += matriz[j][i]
        if suma_columnas != CM:
            cuadrado_magico = False
            break
    return cuadrado_magico

def sumar_diagonal(matriz):
    M = len(matriz)
    N = len(matriz[0])
    CM = N * (N**2 + 1) / 2
    cuadrado_magico = True
    suma_diagonal_1 = 0
    variable_j = 0
    suma_diagonal_2 = 0
    
    for i in range(M):
        suma_diagonal_1 += matriz[i][variable_j]
        variable_j += 1
    
    for i in range(M):
        suma_diagonal_2 += matriz[i][N - i - 1]    
    
    if suma_diagonal_1 != CM or suma_diagonal_2 != CM:
        cuadrado_magico = False
        
    return cuadrado_magico

def verificar_cuadrado_magico(matriz) -> bool:
    M = len(matriz)
    N = len(matriz[0])
    cuadrado_magico = True
    if M == N:
        if sumar_filas() == False or sumar_columnas == False or sumar_diagonal == False:
            cuadrado_magico = False
    else:
        cuadrado_magico = False
                
    return cuadrado_magico

matriz = [[1,2,3],
          [3,4,5],
          [7,8,9]]

print(verificar_cuadrado_magico(matriz))
