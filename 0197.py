lista = []
for i in range(1,5):
    notas = int(input(f'Ingrese la nota numero {i}: '))
    lista.append(notas)
suma = sum(lista)
promedio = suma / 4

print(f'La suma de las 4 notas es: {suma}\nEl promedio de las 4 notas es: {promedio}')