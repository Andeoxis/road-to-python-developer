# Para cerrar con broche de oro esta saga de validaciones avanzadas, vas a resolver este ejercicio tú solo,
# aplicando el contador de intentos de forma correcta (sin resetearlo adentro).

# Enunciado:
# Estás programando el sistema de seguridad para los camiones cisterna que reabastecen de combustible a las sucursales.
# El sistema exige tres datos correctos por seguridad antes de abrir las válvulas:

# Tipo de Combustible: Solo se permite "diesel" o "gasolina".

# Presión de la Válvula: Debe estar en un rango seguro de 20 a 50 PSI.

# Código del Chofer: Solo hay dos choferes autorizados para esta carga, sus códigos son 1010 o 2020 (números enteros).

# Reglas del Sistema:

# El usuario tiene 3 intentos en total (comienza en intentos = 3 afuera).

# Si falla, se le resta 1 intento. Si llega a 0, se activa el break con el mensaje "¡SISTEMA BLOQUEADO POR SEGURIDAD! 🚨".

# Si sale del bucle con éxito, calcula el volumen total: si es "diesel" se despachan 5000 litros, si es "gasolina" 4000 litros.
# Muestra el éxito y los litros despachados.

combustible = input('Escoja el tipo de combustible (diesel / gasolina) ').lower().strip()
presion = int(input('Escoja la presion a configurar (debe estar en el rango de 20 a 50 PSI) '))
codigo = input('Digame su codigo de chofer (sus codigos son 2020 o 1010) ').strip()
intentos = 3

while not ((combustible == 'diesel' or combustible == 'gasolina') and (20 < presion < 50) and (codigo == '2020' or codigo == '1010')):
    print('Alguno de los datos que pusiste esta mal.')
    intentos -= 1
    print(f'Te quedan un total de {intentos} intentos.')

    if intentos == 0:
        print('Lo sentimos ya no le quedan intentos')
        print('Usted fue bloqueado.')
        break

    print('Intente nuevamente.')
    combustible = input('Escoja el tipo de combustible (diesel / gasolina) ').lower().strip()
    presion = int(input('Escoja la presion a configurar (debe estar en el rango de 20 a 50 PSI) '))
    codigo = input('Digame su codigo de chofer (sus codigos son 2020 o 2020) ').strip()

if intentos > 0:
    print('Excelente ya tus datos fueron anotados.')
