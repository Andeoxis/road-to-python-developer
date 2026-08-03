def accion_semaforo(color):
    match dato:
        case 'verde':
            return 'Avanzar'
        case 'rojo':
            return 'Detenerse'
        case 'amarillo':
            return 'Precausion/frenar'
        case _:
            return 'ERROR. Dato errorneo'

dato = input('Ingrese que color tenemos (verde/amarillo/rojo):\n')
respuesta = accion_semaforo(dato)
print(f'Tu debes: {respuesta}')