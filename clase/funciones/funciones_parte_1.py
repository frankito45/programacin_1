
def  return_data(data) -> None:
    """muestra un texto

    Args:
        data (_type_): muestra por consola cualquier tipo de dato que le mandes
    """
    print('info:{}'.format(data))

def validation_float(num)->float:
    """

    Args:
        num (float):conpara si la variavle es de tipo flotante  

    Returns:
        bool: ture si es un numero con coma
    """    
    flag = False

    while type(num) != float:
        num = input('ingrese un numero flotante: ')
        for x in num:
             if x == '.' or ',':
                  flag = True
        
    return flag

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
    flag = False
    if num == 0 and num / 2 != 0:
        flag = True
        
    return flag
        


def numero_mayor(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    
    elif num2 > num1 and num2 > num3:
        return num2
    
    else:
        return num3

def portenci_de_numero(base,exponente):
    base ** exponente
    pass