# Imagina que estás armando un prototipo de brazo robótico y necesitas configurar el voltaje que se le envía a
# los servomotores mediante programación. Por seguridad de las piezas, el servomotor solo opera de forma segura en un
# rango de 5 a 9 voltios. Si el usuario ingresa un voltaje menor a 5 o mayor a 9, el motor se puede quemar o no prender,
# por lo que el sistema debe exigir que se corrija.

configuracion_del_usuario_en_voltios = int(input('Ingrese la cantidad de voltios a configurar (rango correcto es de 5 a 9 voltios)'))
while not (5 < configuracion_del_usuario_en_voltios < 9):
    print('Rango incorrecto, intente de nuevo')
    configuracion_del_usuario_en_voltios = int(input('Ingrese la cantidad de voltios a configurar (rango correcto es de 5 a 9 voltios)'))
print('Rango correcto, enviaste los voltios necesarios.')