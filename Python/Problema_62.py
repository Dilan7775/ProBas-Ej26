#Problema62

def calcular_calificacion_final(parcial1, parcial2, parcial3):
    promedio = (parcial1 + parcial2 + parcial3) / 3
    
    promedio = round(promedio, 2)
    
    if promedio < 6.0:
        print(f"Tu promedio es {promedio}: ¡Te vas a extra!")
    else:
        print(f"Tu promedio es {promedio}: ¡Felicidades, aprobaste!")
        
    return promedio

nota_final_1 = calcular_calificacion_final(8, 9, 7)

nota_final_2 = calcular_calificacion_final(5, 4, 6)