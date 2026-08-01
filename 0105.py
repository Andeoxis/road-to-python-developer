lista = []
while True:
    print('--- SISTEMA DE INGRESO PEJAES ---')
    print('1. Auto')
    print('2. Moto')
    print('3. Camion')
    print('4. Tractor')
    print('5. Salir')
    
    try:
        tipo_de_vehiculo = int(input('Ingrese algun numero (1-5):\n'))
    except ValueError:
        print('ERROR: Solo puede colocar numeros, no letras.')
        continue
        
    match tipo_de_vehiculo:
        case 1:
            vehiculo = 100
            print('Usted selecciono Auto.')
        case 2:
            vehiculo = 100
            print('Usted selecciono Moto.')
        case 3:
            vehiculo = 400
            print('Usted selecciono Camion.')
        case 4:
            vehiculo = 400
            print('Usted selecciono tractor.')
        case 5:
            print('Saliendo del sistema...')
            break
        case _:
            print('ERROR. Intente nuevamente.')
            continue
        
 
    match vehiculo:
        case 400:
            descuento = int(400 * 0.5)
            total = int(vehiculo - descuento)
            print(f'Usted deberia pagar {vehiculo}, pero tienes un des cuento.')
            print(f'Tu descuento es de: {descuento}.')
            print(f'Debes pagar un total de: {total}')
            lista.append(total)
        case 100:
            print('Usted no tiene descuento')
            print(f'Debes pagar un total de: {vehiculo}')
            lista.append(vehiculo)

print('\n--- RESUMEN FINAL DE LA LISTA ---')
for elemento in lista:
    print(elemento)
    
print('Hasta luego.')
print('Salida con exito.')