# Imagina que estás programando el sistema de reservas para un complejo deportivo.
# El usuario tiene que elegir qué tipo de cancha quiere reservar: "sintetica" o "parquet" (para fútsal).
# Si escribe cualquier otra cosa (como "tierra", "cemento" o texto vacío),
# el programa le debe decir que no es válido y obligarlo a elegir de nuevo.

# Instrucciones para tu archivo 019.selector_cancha.py:

# Afuera del bucle: Pide al usuario que elija el tipo de cancha por primera vez usando input(), aplicando .lower().strip().

# La condición del while: Crea un while que atrape al usuario si lo que escribió NO es "sintetica" Y TAMBIÉN NO es "parquet".

# Pista: Usa el operador != y conéctalos con un and (igualito al ejercicio de la factura).

# Adentro del bucle:

# Muestra un mensaje de error: "Tipo de cancha no disponible, intenta de nuevo."

# Vuelve a pedir el input guardándolo en la misma variable para que el bucle tenga la opción de cerrarse.

# Afuera del bucle: Si el programa logra salir del while, significa que la opción ya es correcta.
# Usa un if-else para mostrar el precio final:

# Si eligió "sintetica", imprime: "Reserva confirmada. El precio es de 150 Bs."

# Si eligió "parquet", imprime: "Reserva confirmada. El precio es de 100 Bs."

eleccion_cancha_de_futbol = input('Eliga una de las dos canchas que tenemos. (sintetica / parquet)').lower().strip()
while eleccion_cancha_de_futbol != 'sintetica' and eleccion_cancha_de_futbol != 'parquet':
    print('Dato erroneo, intenta de nuevo papuchin.')
    eleccion_cancha_de_futbol = input('Eliga una de las dos canchas que tenemos. (sintetica / parquet)').lower().strip()
if eleccion_cancha_de_futbol == 'sintetica':
    print('Perfecto, la reserva esta hecha en la cancha sintetica, el precio es de 150 bs')
else:
    print('Perfecto la reserva esta hecha en la cancha de parquet, el precio es de 100 bs')