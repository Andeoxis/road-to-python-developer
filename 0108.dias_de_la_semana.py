def obtener_dia(dia):
    match dato:
        case 'lunes' | 'martes' | 'miercoles' | 'jueves' | 'viernes':
            return 'Dia laboral normal.'
        case 'sabado' | 'domingo':
            return 'Fin de semana, a descansar.'
        case _:
            return 'Dato incorrecto.'

dato = input('Inserte un dia de la semana:\n').lower().strip()
respuesta = obtener_dia(dato)
print(f'Tu respuesta para hoy es: {respuesta}')
