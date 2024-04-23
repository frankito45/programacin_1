
from validaciones import validacion_int, validacion_string 


def get_float(num: float, mensaje_error:str, minimo:float, maximo:float, reintento: float)-> float|None:
    'obtiene un flotante'
    validate = validacion_int(num, minimo, maximo, reintento, mensaje_error)
    if validate:
        parse_float = num
        return parse_float



def get_int(num:int , mensaje_error:str, minimo:int, maximo:int, reintento: int)-> int|None:
    'obtiene un numero entero'
    validate = validacion_int(num, minimo, maximo, reintento, mensaje_error)
    if validate:
            parse_int = num
            return parse_int

     


def get_string(text:str, min_lon, max_long, isalpha = False) -> str|None:
    'obtiene un string'
    validate = validacion_string(text, min_lon , max_long , isalpha)
    if validate:
        parse_text = text
        return parse_text
