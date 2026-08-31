print('\n---- Bienvenido al sistema de sesiones ----')
intentos = 5
for i in range(1, 6):
    print('''
    Seleccione alguna de las siguentes opciones:
    1. Iniciar sesion
    2. Crear cuenta
    3. Salir''')
    opcion = ''.join(input('->').split()).lower()

    match opcion:
        case '1' | 'iniciarsesion':
            print('Iniciando sesion...')
            break
        case '2' | 'crearcuenta':

            print('Creando cuenta...')
            while True:
                usuario = input('Invente algun nombre de usuario con 5 caracteres minimo: ')
                if len(usuario) >= 5:
                    contrasena = input('Ingrese alguna contrasena mayor a 5 caracteres: ')
                    if len(contrasena) > 5:
                        print('Creacion de cuenta exitosa')
                        break
                    else:
                        print('Contrasena incorrecta')
                else:
                    print('Nombre de usuario incorrecto')
            intentos = intentos - 1

        case '3' | 'salir':
            print('Saliendo del sistema...')
            break
        case _:
            print('Error dato erroneo')
            intentos = intentos - 1
            print(f'Tienes {intentos} intentos')
            if intentos == 0:
                print('Uy... Te quedaste sin intentos, bye moichito jiji')