my_list = [23,454,6,3,23,-345,2,-1]



def encontrar_negarivo(lista: list):
        
    negativo = False
    for i in range(len(my_list)):
        if my_list[i] < 0 :
            negativo = True
            break
    return negativo

