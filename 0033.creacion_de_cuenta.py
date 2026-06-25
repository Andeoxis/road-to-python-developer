import sys

cuenta = 'vasquez'
contrasena = '1234'

print('----- Bienvenido al sistema de la incubadora de huevos -----\n')
print('''Antes de entrar debe tener una cuenta...
Seleccione alguno de los insisos.
1. Tiene cuenta (Entrar)
2. Crear cuenta (Crear)
3. Salir del sistema (Salir)''')
seleccion = input().lower().strip()


if seleccion == '1' or seleccion == 'entrar':
    print('Perfecto. Ingresemos a su cuenta')


    while True:
        logear = input('Ingrese su cuenta: ')
        if logear == cuenta:
            print('Cuenta correcta.')
            break
        else:
            print('Cuenta incorrecta. Intenta nuevamente.')

    while True:
        contra = input('Ingrese su contrasena: ')
        if contra == contrasena:
            print('Contrasena correcta.')
            break
        else:
            print('Contrasena incorrecta. Intente nuevamente.')

elif seleccion == '2' or seleccion == 'crear':
    print('Perfecto. Creemeos una cuenta propia')
    
    while True:
        cuenta = input('Crea una cuenta (minimo 6 caracteres) ')
        if len(cuenta) >= 6:
            print('Perfecto. Cuenta creada.')
            break
        else:
            print('Intenta nuevamente.')

    while True:
        contrasena = input('Crea una contrasena (minimo de 8 caracteres) ')
        if len(contrasena) >= 8:
            print('Perfecto. Contrasena creada')
            break
        else:
            print('Intenta nuevamente.')
    
    print('Cuenta creada con exito.')
    
    while True:
        log = input('Ingresa a tu cuenta ')
        if cuenta == log:
            print('Cuenta correcta.')
            break
        else:
            print('Cuenta incorrecta. Intenta nuevamente.')
            


    while True:
        contra = input('Ingresa tu contrasena ')
        if contrasena == contra:
            print('Contrasena correcta.')
            break
        else:
            print('Contrasena incorreecta. Intenta nuevamente.')
    


elif seleccion == 'salir' or seleccion == '3':
    print('Perfecto. Saliendo del sistema, chau.')
    sys.exit()





    







        

    