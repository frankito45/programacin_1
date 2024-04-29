

def par_inpar(num) -> bool:
    'recive un numero si es par devuelve true '
    flag = True
    if num == 0 or num % 2 != 0:
        flag = False
        
    return flag



def encontrar_maximo_indice(lista:list) -> None:
    'encuentra el mayo numero de la lista '
    maximo = 0

    for i in range(len(lista)):
        if maximo < lista[i] or maximo == 0:
            maximo = i

    return maximo


def encontrar_menor_indice(lista:list) -> None:
    'encuenta el menot  indice de la lista '
    menor = 0

    for i in range(len(lista)):
        if menor < lista[i] or menor  == 0:
            menor = i

    return menor




def envent_interface(flag,event):
    if  flag:
        event
    else:
        print("primero ingrese los numero ( a )")
