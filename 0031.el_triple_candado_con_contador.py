# Imagina que estás mejorando el sistema de facturación para tu negocio de pollos.
# El usuario va a registrar un despacho y el sistema le va a exigir tres datos correctos:

# El producto: Solo se acepta "pollo" o "huevo".

# El destino: Solo hacemos envíos a "sacaba" o "quillacollo" (las sucursales autorizadas).

# El peso del camión: Por normas de tránsito, el camión cargado debe pesar entre 1000 y 5000 kilos.

producto = input('Ingrese el producto que desea añadir (pollo / huevo): ')
destino = input('Ingrese el destino (sacaba / quillacollo): ')
peso = int(input('Cuánto pesa el camión (rango de 1000 a 5000 kg): '))

intentos = 3

while not ((producto == 'pollo' or producto == 'huevo') and (destino == 'sacaba' or destino == 'quillacollo') and (1000 <= peso <= 5000)):
    print('\n❌ Alguno de tus datos falló.')
    intentos -= 1
    print(f'Te quedan {intentos} intentos.')
    
    # 1. CONTROL DE EMERGENCIA: Si se acaban los intentos, morimos aquí adentro
    if intentos == 0:
        print('🔒 Lo sentimos, llegó al número máximo de intentos. Usted queda BLOQUEADO.')
        break  # Rompe el while por completo
        
    # 2. EL RE-INPUT: Si NO llegó a 0 intentos, recién le pedimos los datos de nuevo
    print('Intenta nuevamente:')
    producto = input('Ingrese el producto (pollo / huevo): ')
    destino = input('Ingrese el destino (sacaba / quillacollo): ')
    peso = int(input('Cuánto pesa el camión (1000 a 5000 kg): '))

# 3. AFUERA DEL BUCLE: Filtramos cómo salimos (¿Por éxito o por bloqueo?)
if intentos > 0:
    print('\n✅ Perfecto, los datos ingresados son los correctos. ¡Despacho aprobado!')




# producto = input('Ingrese el producto que desea anadir (pollo / huevo): ')
# destino = input('Ingrese el destino (sacaba / quillacollo)')
# peso = int(input('Cuanto pesa el camion (si o si debe estar en el rango de 1000kg y 5000kg)'))
# intentos = 3
# while not ((producto == 'pollo' or producto == 'huevo') and (destino == 'sacaba' or destino == 'quillacollo') and (1000 <= peso <= 5000)):
#     print('Alguno de tus datos fallo, intenta nuevamente ')
#     intentos -= 1
#     print(f'Tienes {intentos} intentos de 3.')
#     if intentos == 0:
#         print('Lo sentimos, llego al numero maximo de intentos. usted queda bloqueado.')
#         break
# print('Perfecto, los datos ingresados son los correctos.')