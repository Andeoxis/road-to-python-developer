errores = 0
while True:
    try:
        pr = int(input('Coloca tu record del gym:\n'))
        if 0 < pr < 250:
            print('Felicidaes, nuevo record registrado.')
            break
        else:
            print('ERROR: Intenta de nuevo.')
            errores += 1
    except ValueError:
        print('ERROR: No se permiten otros caracteres que no seaa numeros.')
        print('Intenta de nuevo.')
        errores += 1
    
print(f'Tu record maximo es {pr} kg')
if errores > 0:
    print(f'Te equivocaste {errores} veces.')