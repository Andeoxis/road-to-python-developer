# Imagina que estás en la puerta del concierto de Sin Bandera controlando el acceso a la zona VIP exclusiva.
# Para que el guardia deje pasar a alguien, se deben cumplir dos condiciones de éxito:

# La credencial: El invitado debe mostrar su pase. Solo son válidos los pases de tipo "artista" o "staff".

# El código de seguridad: Cada invitado VIP tiene un código numérico impreso que debe estar entre el 100 y el 500
# (por ejemplo, el código 250 pasa, pero el 99 o el 600 se quedan afuera).

# Si se equivocan en el pase O su código no está en el rango permitido,
# el sistema bloquea el torniquete y vuelve a pedir ambos datos.

credencial = input('Muestra tu pase (artista / staff): ')
codigo_de_seguridad = int(input('Digame cual es su codigo numerico (debe estar entre 100 y el 500): '))
while not ((credencial == 'artista' or credencial == 'staff') and (100 < codigo_de_seguridad < 500)):
    print('Se bloqueo el torniquete, vuelva a ingresar sus datos.')
    credencial = input('Muestra tu pase (artista / staff): ')
    codigo_de_seguridad = int(input('Digame cual es su codigo numerico (debe estar entre 100 y el 500): '))
print('acceso permitido, disfruta la fiesta brother.')