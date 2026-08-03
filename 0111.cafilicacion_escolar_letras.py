def evaluar_nota(letra):
    match dato:
        case 'a':
            return 'Excelente trabajo.'
        case 'b':
            return 'Buen trabajo.'
        case 'c':
            return 'Aprobado.'
        case 'd' | 'f':
            return 'Reprobado.'
        case _:
            return 'ERROR. Dato erroneo.'

dato = input('Ingrese su nota (A/B/C/D/F):\n').lower().strip()
respuesta = evaluar_nota(dato)
print(f'Tu estas: {respuesta}')