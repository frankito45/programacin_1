class boligrafo:
    def __init__(self, grosor_punta:str, color:str):
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = 80

    def escribir_texto(self,texto):
        count = 0
        for i in range(len(texto)):
            if texto[i] != " ":
                count += 1
        if self.cantidad_tinta > count:
            self.cantidad_tinta -=  count    
            return texto

    def recarcar():
        pass


# Deberá validar si el bolígrafo cuenta con la tinta suficiente para escribir el texto: La tinta a ser gastada corresponde a la cantidad de caracteres (Ej: el texto “hola” gasta 4 de tinta, si el trazo es fino. Si es grueso gasta el doble )
# En caso de contar con la tinta suficiente, deberá restarse la cantidad del atributo cantidad_tinta y devolver una cadena con el texto recibido por parámetro.
