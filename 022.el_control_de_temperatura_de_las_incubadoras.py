# Imagina que estás automatizando el sistema de control para una incubadora de huevos en tu negocio de pollos.
# Para que los huevos se desarrollen bien, la temperatura configurada por el usuario debe estar entre 35°C y 40°C.
# Si el operario mete una temperatura menor a 35 O mayor a 40,
# el sistema está en peligro y el programa debe exigir que se corrija el dato.

temperatura_configurada_por_el_usuario = int(input('Ingrese la temperatura configurada. (debe estar entre 35C y 40C)'))
while temperatura_configurada_por_el_usuario < 35 or temperatura_configurada_por_el_usuario > 40:
    print('La temperatura que ingresaste sale del rango, vuelve a intentarlo')
    temperatura_configurada_por_el_usuario = int(input('Ingrese la temperatura configurada. (debe estar entre 35C y 40C)'))
print('Muy bien, la temperatura esta en el rango correcto')