from funciones import opcion
from administrador import menu_administrador
from cliente import menu_cliente

print('---- BIENVEIDO AL SISTEMA ----')

while True:
    try:

        print('Escoge alguna de las siguentes opciones solo numeros (1 - 2): ')
        print('1. Cliente')
        print('2. Administrador')
        opciones = int(input(''))
        if opciones not in (1, 2):
            raise ValueError
        name = input('Ingrese su nombre de usuario: ')
        contrasena = input('Ingrese su contrasena: ')
        resultado = opcion(opciones, name, contrasena)
        if resultado == False:
            raise ValueError
        print(resultado)
        print()  
        break
        
    except ValueError:
        print('Error. Algo fallo...')
        print('Intente nuevamente.')
        print()

if resultado == 'Logeo exitoso cliente':
    menu_cliente()
elif resultado == 'Logeo exitoso administrador':
    menu_administrador()