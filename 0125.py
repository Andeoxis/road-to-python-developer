print('\n==============================')
print('    BIENVENIDO AL WARCRAFT')
print('==============================\n')

name = input('Ingrese su nombre de jugador: ')

while True:
    try:
        print(f'Seleccione que personaje desea elegir {name}:')
        print('1. Mago')
        print('2. Orco')
        print('3. Humano')
        personaje = input('-> ').lower().strip()

        match personaje:
            case '1' | 'mago':
                print(f'Perfecto {name}, ahora eres un Mago')
                personaje = 'mago'
            case '2' | 'orco':
                print(f'Perfecto {name}, ahora eres un Orco')
                personaje = 'orco'
            case '3' | 'humano':
                print(f'Perfecto {name}, ahora eres un Humano')
                personaje = 'humano'
        print()
        break
    except ValueError:
        print('Algo fallo...')
        print(f'Intente nuevamente {name}')


while True:
    try:
        print('Elige el nivel de dificultad que deseas:')
        print('Facil')
        print('Intermedio')
        print('Dificil ')
        dificultad = input('->').lower().strip()
        match dificultad:
            case 'facil':
                print(f'La dificultad seleccionada es: Facil')
            case 'intermedio':
                print(f'La dificultad seleccionada es: Intermedia')
            case 'dificil':
                print(f'La dificultad seleccionada es: Dificil')
        print()
        break
    except ValueError:
            print('Algo fallo...')
            print(f'Intente nuevamente {name}')


if personaje == 'orco':
    print('Tus caracteristicas son:')
    print('Vida: 150')
    print('Ataque: 10')
    print('Velocidad: 10')
    vida = 150
    ataque = 10
    velocidad = 10
elif personaje == 'mago':
    print('Tus caracteristicas son:')
    print('Vida: 100')
    print('Ataque: 15')
    print('Velocidad: 10')
    vida = 100
    ataque = 15
    velocidad = 10
elif personaje == 'humano':
    print('Tus caracteristicas son:')
    print('Vida: 100')
    print('Ataque: 10')
    print('Velocidad: 15')
    vida = 100
    ataque = 10
    velocidad = 15


while True:
    try:
        print('\nIniciando juego...')
        print(f'{name} Escoge entre estos dos caminos: Bueno o malo')
        camino_bueno_y_malo = input('-> ').lower().strip()
        if camino_bueno_y_malo == 'bueno':
            print('No recibes dano, el camino del bien siempre sera el correcto')
            print(f'\nTus caracteristicas son:')
            print(f'Vida: {vida}')
            print(f'Ataque: {ataque}')
            print(f'Velocidad: {velocidad}')
            break
        elif camino_bueno_y_malo == 'malo':
            print('Recibiste 10 de dano, el mal nunca es el camino correcto...')
            print(f'\nTus caracteristicas son:')
            print(f'Vida: {vida - 10}')
            print(f'Ataque: {ataque}')
            print(f'Velocidad: {velocidad}')
            break
    except ValueError:
        print('Algo fallo...')
        print(f'Intente nuevamente {name}')


print('Ya tomaste el camino que te corresponde...')
print('Caminas por el bosque...')
print('Ya se hizo de noche...')


while True:
    try:
        print('Decide si acampar o seguir caminando: ')
        decidir_acampar_o_caminar = input('-> ').lower().strip()
        if decidir_acampar_o_caminar == 'acampar':
            print('Escogiste bien.')
            print('Evitaste a los monstruos.')
            print('Ganaste.')
            break
        elif decidir_acampar_o_caminar == 'seguir caminando' or decidir_acampar_o_caminar == 'caminar' or decidir_acampar_o_caminar == 'caminando':
            print('Escogiste mal')
            print('Enfrente tuyo hay un monstruo')
            while True:
                try:
                    print('Tienes dos opciones a eleccion: Pelear/huir')
                    elecciones = input('-> ').lower().strip()
                    if elecciones == 'pelear':
                        print('Perdiste el monstruo te quito toda tu vida')
                        print('Termino el juego.')
                        break
                    elif elecciones == 'huir':
                        print('Te salvaste el monstruo es muy pesado y prefiero no seguirte')
                        print('Ganaste el juego te salvaste por poco.')
                        break
                except ValueError:
                    print('Algo fallo...')
                    print(f'Intente nuevamente {name}')
            break

    except ValueError:
        print('Algo fallo...')
        print(f'Intente nuevamente {name}')
