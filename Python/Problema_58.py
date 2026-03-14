#Problema58

import random

def llenar_lista_aleatoria(cantidad, inicio, fin):
    lista = []
    for _ in range(cantidad):
        numero = random.randint(inicio, fin)
        lista.append(numero)
    return lista

mi_lista = llenar_lista_aleatoria(10, 1, 100)
print(mi_lista)