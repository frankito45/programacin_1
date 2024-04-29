from input_package.input import * 

from package_Array.generales import *
from package_Array.especifica import *



flag = False
lista = [0] * 10 
while True:
    opcion = input('''
        a: ingreso de 10 números enteros entre -1000 y 1000.\n
        b: Mostrar la cantidad de números positivos y negativos.\n
        c: Mostrar la sumatoria de los números pares.\n
        d:  Informar el mayor de los números impares.\n
        e:  Listar todos los números ingresados.\n
        f: Listar todos los números pares.\n
        g:Listar los números de las posiciones impares.\n  
        h: Salir
                   ingrese su opcion : ''')
    
    match opcion:
        case 'a':
            flag = True
            for i in range(len(lista)):

                num = int(input('seleccione un numero entre -1000 y 1000: '))
                parse_num = get_int(num,'numero no valido',-1000,1000,10)
                lista[i] = parse_num


        case 'b':
                envent_interface(flag,total_positovo_negativo(lista))
        case 'c':
            envent_interface(flag, sumar_las_paridades(lista))
              
        case 'd':
            envent_interface(flag,mayor_num_impar(lista))

        case 'e':
            envent_interface(flag,mostrar_lista(lista))

        case 'f':
            envent_interface(flag, mostrar_numeros_pares(lista))

        case 'g':
            envent_interface(flag, posiciones_impares(lista))

        case 'h':
              
              break
        

