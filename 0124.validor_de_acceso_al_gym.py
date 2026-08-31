def validor_de_acceso_al_gym(edad):
    'Validor de edad para acceder al gym.'
    if edad >= 18:
        return 'Tu edad es correcta puedes pasar'
    return 'Tu edad es incorrecta no puedes pasar'

while True:
    try:
        print(f'{validor_de_acceso_al_gym.__doc__}')
        edades = int(input('Ingrese su edad:\n'))
        print(f'Respuesta: {validor_de_acceso_al_gym(edades)}')
        break
    except ValueError:
        print('Error. Dato erroneo.')
        print('Intenta nuevamente.')
        print()


