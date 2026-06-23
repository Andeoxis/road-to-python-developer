# Ejercicio 3: El Guardián de la Clave Secreta
# Enunciado:
# Imagina que quieres entrar a una habitación secreta, pero hay un guardia en la puerta.
# El guardia te va a pedir la palabra clave una y otra vez (bucle infinito) hasta que adivines la palabra correcta.

# La palabra clave secreta es "python123".

# Debes escribir un programa que haga lo siguiente:

# Inicie un bucle while True.

# Adentro del bucle, pida al usuario que escriba la contraseña usando un input().

# Evalúe con un if:

# Si la contraseña es INCORRECTA: Debe mostrar un mensaje que diga "Acceso denegado. Intente de nuevo.".
# Como no hay un break en esta parte, el while True va a volver a empezar y le va a pedir la contraseña otra vez.

# Si la contraseña es CORRECTA: Debe mostrar un mensaje que diga "¡Acceso concedido! Bienvenido."
# y justo después usar un break para detener el bucle.

# # Fuera del bucle (abajo del todo), pon un último print() que diga "Fin del programa.".


while True:
    clave_secreta = input('Dime cual es la clave secreta: ')
    if clave_secreta == 'python123':
        print('Acceso permitido')
        break
    else:
        print('Acceso denegado, intenta de nuevo')

print('Fin del programa')
        
