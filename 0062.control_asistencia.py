temprano = 0
tarde = 0
error = 0
for trabajador in range(1, 7):
    while True:
        try:
            asistencia = int(input(f'Trabajador N{trabajador}: Ingrese 1 si llego tarde, e ingrese 2 si llego temprano: '))

            if asistencia == 1:
                print(f'Usted llego tarde Trabajador N{trabajador}.')
                tarde += 1
                print()
                break
                
            elif asistencia == 2:
                print(f'Usted llego temprano felicidades Trabador N{trabajador}.')
                temprano += 1
                print()
                break
            else:    
                print('Dato incorrecto... Por favor intente de nuevo.')
                error += 1
                print()

        except ValueError:
            print('ERROR: No se permiten letras, solo numeros.')
            print('Intente de nuevo.')
            error += 1
            print()

print(f'Llegaron temprano {temprano}\nLlegaron tarde {tarde}\nDatos erroneos {error}')

