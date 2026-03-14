#Problema63

numeros = [2, 4, 6, 8]
def obtener_cuadrados(lista_original):
    lista_cuadrados = []
    for numero in lista_original:
        cuadrado = numero ** 2  
        lista_cuadrados.append(cuadrado)
    return lista_cuadrados

print(obtener_cuadrados(numeros)) 