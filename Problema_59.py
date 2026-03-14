#Problema59

def calcular_sumatoria(lista):
    total = 0  
    for numero in lista:
        total += numero  
    return total

numeros = [10, 20, 30, 40]
resultado = calcular_sumatoria(numeros)
print(f"La suma total es: {resultado}")