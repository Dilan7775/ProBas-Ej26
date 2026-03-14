#Problema69

def es_correo_valido(email):
    if "@" in email:
        return True
    else:
        return False

def main():
    email = input("Por favor, ingresa tu dirección de email: ")
    
    if es_correo_valido(email):
        print("La dirección de correo es válida.")
    else:
        print("La dirección de correo NO es válida. Debe contener el símbolo '@'.")

if __name__ == "__main__":
    main()