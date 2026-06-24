# Las '\n' Hacen que recorras un espacio, cuando lo haces al principio de algo que quieres escribir entonces hara un espacio arriba, y si lo haces a la mitad o menos de la mitad o a final,
# este recorrera un espacio hacia abajo
print('''\n---------- Bienvenido al sistema de registro de animales ----------\n
Dime que animales traes contigo para poder llevar registro de los animales que hay en la enbarcacion.
1. perro
2. gato
3. pajaro''')

print('''Dime cual es la opcion que mas te gusta.
1. 
2.
3.
4.
5.''')
opcion = int(input('Que opcion es la que te gusto mas: '))
print(f'La opcion que mas te gusto es {opcion}, felicidades.')
print(f'Lo que haremos con la opcion {opcion}, sera sumarle numeros')
print(f'La operacion que se realizo es la siguiente 2 + {opcion} = ...')
opcion = opcion + 2
print(f'La respuestas es opcion = {opcion}')