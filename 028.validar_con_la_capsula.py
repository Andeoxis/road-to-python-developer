# Estás programando la preventa de boletos para un concierto local en Cochabamba
# (como el de Sin Bandera o Wara Sinfónico). El sistema tiene dos reglas estrictas de éxito:

# El sector: Solo existen dos sectores válidos: "vip" o "general".

# La edad: Por seguridad del evento, solo pueden comprar personas que tengan entre 18 y 65 años.

sector = input('Que sector eres? (vip / general: )')
edad = int(input('Ingresa la edad que tengas (debes tener entre 18 y 65 anos para ingresar )'))
while not ((sector == 'vip' or sector == 'general') and (18 < edad < 65)):
    print('Alguno de los datos que pusiste esta mal, o quizas ambos estan mal. intente nuevamente')
    sector = input('Que sector eres? (vip / general: )')
    edad = int(input('Ingresa la edad que tengas (debes tener entre 18 y 65 anos para ingresar )'))
print(f'perfecto tu edad es de {edad} y tu sector es de {sector}')