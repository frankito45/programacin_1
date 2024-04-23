
def  return_data(data) -> None:
    print('info:{}'.format(data))

def validation_float(num)->float:
    while type(num) != float:
        num = input('ingrese un numero flotante: ')

        if not num.isdigit() and not num.isalnum():
            return num
    return num

def validation_int(num)->int:
    while type(num) != int:
        num = input('ingrese un numero flotante: ')

        if  num.isdigit() and not num.isalnum():
            return num
    return num

def validation_text(data)->str:
    while type(data) != int:
        data = input('ingrese un texto: ')

        if  not data.isdigit() and  data.isalnum():
            return data
        
    return data

def formate_float(num):
        parse_float = validation_float(num)
        return_data(parse_float)

def formate_int(num):
        parse_int = validation_int(num)
        return_data(parse_int)
def formate_text(data):
        parse_tex = validation_text(data)
        return_data(parse_tex)

import math
def calcular_area(radio=int):
    area = math.pi ** radio
    return area 

def par_inpar(num):
    num = validation_int
    if num == 0 and num / 2 != 0:
        mensaje = 'su numero no es par'
        return_data(mensaje)
    else:
        mensaje = 'su numero es par '
        return_data(mensaje)


def numero_mayor(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    
    elif num2 > num1 and num2 > num3:
        return num2
    
    else:
        return num3

def portenci_de_numero(base,exponente):
    pass