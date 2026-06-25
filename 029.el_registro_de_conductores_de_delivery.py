# Vamos a usar este superpoder en un ejercicio de tu nivel.
# Imagina que estás programando la aplicación de delivery para los despachos de tu negocio.
# Para registrar a un nuevo conductor de motocicletas, el sistema exige dos condiciones de éxito:

# El vehículo: El conductor debe registrar qué maneja.
# Solo se acepta "moto" o "torito" (esos trimóviles motorizados).

# Los años de experiencia: Para evitar accidentes con los pedidos,
# el conductor debe tener entre 2 y 10 años de experiencia manejando.

vehiculo = input('Ingrese que vehiculo usa (auto / moto): ')
anos_de_exp = int(input('Cuantos anos de exp tiene (debe tener entre 2 y 10 anos de exp manejando: )'))
while not ((vehiculo == 'auto' or vehiculo == 'moto') and (2 < anos_de_exp < 10)):
    print('Alguno de tus datos esta mal, inteta de nuevo')
    vehiculo = input('Ingrese que vehiculo usa (auto / moto): ')
    anos_de_exp = int(input('Cuantos anos de exp tiene (debe tener entre 2 y 10 anos de exp manejando: )'))
print('Perfecto tu puedes trabajar para delivery.')