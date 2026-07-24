intentos_restantes = 5

for i in range(intentos_restantes):
    contrasena = input('Ingresa tu contraseña:\n')
    
    if contrasena == 'hola123':
        print('Contraseña correcta.')
        break
    elif contrasena == 'admin123':
        print('Contraseña del administrador correcta.')
        break
        
    intentos_restantes -= 1
    
    # Validación inmediata del último intento
    if intentos_restantes == 0:
        print('Lo sentimos, ya no te quedan intentos...')
        print('Saliendo del sistema...')
        break  # Rompe el ciclo por seguridad
        
    print('Contraseña incorrecta, intente nuevamente.')
    print(f'Te quedan {intentos_restantes} intentos.')
