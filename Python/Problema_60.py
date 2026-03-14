#Problema60

def calcular_sumatoria(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def calcular_promedio(lista):
    if not lista:
        return 0
    
    suma = calcular_sumatoria(lista)
    promedio = suma / len(lista)
    
    return promedio

mi_lista = [10, 20, 30, 40, 50]
resultado = calcular_promedio(mi_lista)

print(f"El promedio es: {resultado}")