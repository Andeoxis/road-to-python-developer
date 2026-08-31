def password(contrasena):
    """Validador de contrasenas con True y False"""
    return len(contrasena) > 8


while True:
    try:
        print(f"\n{password.__doc__}")
        contra = input("Ingrese contrasena con solo letras: ")

        # 1. Filtro: Solo letras permitidas
        if not contra.isalpha():
            raise ValueError

        # 2. Validación de longitud (> 8 caracteres)
        if password(contra):
            print("Respuesta: True -> Contraseña válida y segura.")
            break  # Solo se sale si cumple las letras Y los > 8 caracteres
        else:
            print("Respuesta: False -> La contraseña es muy corta (debe tener más de 8 letras).")

    except ValueError:
        print("Error. Dato ingresado de manera erronea (solo se permiten letras, sin números ni espacios).")
        print("Intente nuevamente.")