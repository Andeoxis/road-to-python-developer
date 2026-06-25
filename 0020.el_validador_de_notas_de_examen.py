# Estás programando el sistema para que los docentes de tu universidad suban las notas de los exámenes.
# Las notas válidas en el sistema solo pueden ir desde el 0 hasta el 100 (puntos).
# Si un docente, por error de taipeo, mete una nota negativa (como -5) o una nota mayor a 100 (como 150),
# el programa lo tiene que frenar en la puerta y obligarlo a meter una nota real.

# Instrucciones para tu archivo 020.validador_notas.py:

# Afuera del bucle: Pide la nota convirtiéndola a entero:

# Python
# nota = int(input("Ingrese la nota del examen (0 al 100): "))
# La condición del while: Piensa en español: "¿Cuándo está MAL la nota?". Está mal si la nota es menor a 0 O SINO si la nota es mayor a 100.

# Pista clave en Python:
# Aquí vas a usar el operador or, porque basta con que se cumpla una de las dos desgracias para que el dato sea inválido: while nota < 0 or nota > 100:

# Adentro del bucle:

# Muestra un mensaje de error: "Nota inválida. La nota debe estar entre 0 y 100."

# Vuelve a pedir la nota con su int(input(...)) para actualizar la variable y que el bucle pueda terminar cuando pongan un número correcto.

# Afuera del bucle: Si el programa sale del while, significa que la nota es totalmente legal. Usa condicionales if-elif-else para decirle su estado:

# Si la nota es mayor o igual a 51, imprime: "¡Aprobado! Felicidades."

# Si la nota es menor a 51, imprime: "Reprobado. A estudiar más para la próxima."

nota = int(input('Ingrese la nota del examen: (0 al 100)'))
while nota < 0 or nota > 100:
    print('Solo puedes poner notas del 0 al 100, intenta de nuevo')
    nota = int(input('Ingrese la nota del examen: (0 al 100)'))
if nota >= 51:
    print('Aprobaste! felicidades')
else:
    print('Lo sentimos... reprobaste')