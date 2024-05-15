


empleados = [[None] * 5 for _ in range(3)]
LINEAS = len(empleados)
COLECTIVOS = len(empleados[0])

# print(empleados)


def recorrer_matrizz(matriz):
    for lineas in range(LINEAS):
        for empleados in range(COLECTIVOS):
            print(f'{matriz[lineas][empleados]}',end=' ')
        print(f'{matriz[lineas][empleados]}')
recorrer_matrizz(empleados)

def recorrer_matriz(matriz):
    for fila in range(LINEAS):
        for columna in range(COLECTIVOS):
            legajo = input('ingrese un empleado: ')
            matriz[fila][columna] = legajo
    return matriz
    # print(matriz[columna][fila])




def update_planillas(buscar,actualizar,matriz):
    for i in range(LINEAS):
        for j in range(COLECTIVOS):
            if buscar  == matriz[i][j]:
                matriz[i][j] = actualizar     


# print(empleados)a
recorrer_matriz(empleados)
update_planillas('pepe','pablo',empleados)
print(empleados)
print(recorrer_matrizz(empleados))