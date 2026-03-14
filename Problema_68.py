#Problema68

import math

def es_primo(n):
    if n <= 1:
        return False
    
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False  
            
    return True  

numero = int(input("Introduce un número para verificar si es primo: "))

if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")