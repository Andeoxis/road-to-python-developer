# Imagínate que estás programando el sistema de torniquetes automáticos para el gimnasio donde entrenas.
# El sistema pide dos datos para dejar pasar a un atleta a la zona de musculación:

# La membresía: El cliente debe ingresar qué tipo de pase tiene.
# Las únicas dos opciones válidas en el sistema son "mensual" o "anual".

# La hora de ingreso:El gimnasio solo está abierto en horario seguro desde las 06 hasta las 22 horas
# (usa formato militar de 24 horas como número entero).
# Si alguien intenta ingresar a las 5 de la mañana o a las 23 horas, el sistema lo rebota.

# Si el usuario se equivoca en el tipo de membresía O intenta entrar a una hora no permitida,
# el programa debe dar un mensaje de error y volver a pedir ambos datos de forma infinita hasta que todo esté correcto.

# Al salir del bucle, muestra un mensaje de bienvenida que incluya la hora y su membresía.

membresia = input('Ingresa el tipo de membresia que tienes (mensual / anual): ')
ingreso_al_gym = int(input('Ingresa a la hora que ingresaste (06 hasta las 22 horas)'))
while (membresia != 'mensual' and membresia != 'anual') or not (6 < ingreso_al_gym < 22):
    print('Alguno de los dos datos o uno debe estar mal, intente nuevamente.')
    membresia = input('Ingresa el tipo de membresia que tienes (mensual / anual): ')
    ingreso_al_gym = int(input('Ingresa a la hora que ingresaste (06 hasta las 22 horas)'))
print(f'Perfecto tu membresia es {membresia} e ingresas a las {ingreso_al_gym}.')