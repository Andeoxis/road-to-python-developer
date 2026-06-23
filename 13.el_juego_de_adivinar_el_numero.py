# El programa va a elegir un número secreto al azar entre 1 y 20. El usuario tendrá que intentar adivinarlo.
# El bucle while True se repetirá hasta que el usuario lo adivine,
# pero el programa le dará pistas de si el número secreto es mayor o menor al que ingresó.

# Instrucciones:

# Para que Python elija un número al azar, debes poner esta línea arriba del todo,
# en la primera línea de tu archivo (afuera de todo):

# Python
# import random
# Crea la variable del número secreto antes del while True usando este comando:

# Python
# numero_secreto = random.randint(1, 20)
# Inicia tu bucle while True.

# Pide al usuario que intente adivinar: intento = int(input("Adivina el número (1 al 20): "))

# Evalúa con condiciones:

# Si el intento es igual al numero_secreto: Muestras un mensaje de victoria:
# "¡Felicidades! Adivinaste el número." y usas un break para terminar el juego.

# Si el intento es MENOR al numero_secreto: Muestras una pista:
# "El número secreto es MAYOR. Intenta de nuevo.". (No hay break, vuelve a preguntar).

# Si el intento es MAYOR al numero_secreto: Muestras otra pista:
# "El número secreto es MENOR. Intenta de nuevo.". (No hay break, vuelve a preguntar).

import random

numero_secreto = random.randint(1, 20)
while True:
    intento = int(input('Adivina el numero del (1 al 20): '))
    if intento == numero_secreto:
        print('Felicidades adivinaste el numero secreto') 
        break
    elif intento > numero_secreto:
        print('El numero secreto es menor, intenta de nuevo')
    elif intento < numero_secreto:
        print('El numero secreto es mayor, intente de nuevo')
        