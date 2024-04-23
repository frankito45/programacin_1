



def validacion_int(num:int, minimo:int, maximo:int, reintento:int, mesaje_error) -> bool|None:
    '''valida si el numero es entero segun los parametros dados
    parametros: minimo, maximo, reintentos'''

    parse_int = int(num)
    validacion = True
    contador = 0

    while parse_int < minimo or parse_int > maximo:
        contador += 1
        num = input('ingrese un numero entre los rangos: ')
        parse_int = int(num)

        if contador == reintento:
            print('{}'.mesaje_error)
            validacion = False

    return validacion
        


# Repetir el mismo procedimiento para un dato de tipo float


def validacion_float(num:int, minimo:int, maximo:int, reintento:int, mesaje_error) -> bool|None:
    '''valida si el numero es flotante segun los parametros dados
    parametros: minimo, maximo, reintentos'''

    parse_float = float(num)
    validacion = True
    contador = 0

    while parse_float < minimo or parse_float > maximo:
        contador += 1
        num = input('ingrese un numero entre los rangos: ')
        parse_float = int(num)

        if contador == reintento:
            print('{}'.mesaje_error)
            validacion = False

    return validacion


def validacion_string(text, min_lon,max_long, isalpha) -> str|None:
    '''valida si un texto segun sus parametros 
    min_long: minimo caracter,
    max_long: maximo caracter,
    isalpha: si puede ser alphanumeico
    '''
    validacion = True

    if len(text) < min_lon or len(text) > max_long:
        validacion  = False

    if isalpha:
        validacion = validacion_isapha(text)
        

    
    return validacion   


def validacion_isapha(tex:str):
    flag = False
    for x in tex:
        match x:
            case '1':
                flag = True
                break
            case '2':
                flag = True
                break
            case '3':
                flag = True
                break
            case '4':
                flag = True
                break
            case '5':
                flag = True
                break
            case '6':
                flag = True
                break
            case '7':
                flag = True
                break
            case '8':
                flag = True
                break
            case '9':
                flag = True
                break
            case '0':
                flag = True
                break
    return flag


        

