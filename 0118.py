saldo_inicial = 2000
intentos = 3

# 1. Validación de PIN
while intentos > 0:
    pin = input('Ingrese su pin: ')

    if pin == 'hola123':
        print('Acceso concedido.')
        break
    else:
        intentos -= 1
        print('Acceso denegado.')
        print(f'Le quedan {intentos} intentos.')
        if intentos == 0:
            print('Lo sentimos... hubo demasiados intentos.')
            print('Saliendo del sistema.')
            exit()  # Detiene el programa si se acaban los intentos de PIN

# 2. Retiro de dinero (un solo while)
intentos_dinero = 3
while intentos_dinero > 0:
    try:
        print(f'\nUsted tiene un saldo de {saldo_inicial} Bs.')
        monto_a_retirar = int(input('Inserte el monto que desea retirar: '))
        
        if 0 < monto_a_retirar <= saldo_inicial:
            saldo_inicial -= monto_a_retirar
            print(f'Retirando {monto_a_retirar} Bs.')
            print('Retiro con éxito.')
            print(f'Usted tiene un saldo de {saldo_inicial} Bs.')
            break
        else:
            intentos_dinero -= 1
            print('Lo sentimos, monto fuera de rango.')
            print(f'Le quedan {intentos_dinero} intentos.')
            
    except ValueError:
        intentos_dinero -= 1
        print('Dato erróneo (solo números, no letras).')
        print(f'Le quedan {intentos_dinero} intentos.')

if intentos_dinero == 0:
    print('\nSuperó el límite de intentos para el retiro.')
    print('Saliendo del sistema.')