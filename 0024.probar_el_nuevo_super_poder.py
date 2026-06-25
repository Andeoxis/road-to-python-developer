# Para entrar a una discoteca, la edad permitida en Bolivia debe ser entre 18 y 60 años.
# Si meten una edad fuera de ese rango, el programa los rebota.

edad = int(input('Ingrese la edad que tiene ( para entrar debe ser entre 18 y 60 anos)'))
while not ( 18 < edad < 60 ):
    print('No entras porque no estas en el rango requerido')
    edad = int(input('Ingrese la edad que tiene ( para entrar debe ser entre 18 y 60 anos)'))
print('Puedes ingresar, estas en el rango de edad permitido')