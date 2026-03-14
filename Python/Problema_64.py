#Problema64

def es_multiplo(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    
    if a % b == 0:
        return True
    else:
        return False