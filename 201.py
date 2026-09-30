numeros = [10, 20, 30, 40, 50]
buscado = int(input('Ingrese el numero a buscar: '))
encontrado = False
posicion = 0
for i in range(len(numeros)):
    if numeros[i] == buscado:
        encontrado = True
        posicion = i
        break
if encontrado:
    print(f'El numero {buscado} se encuentra en el indice {posicion}.')
else:
    print(f'El numero {buscado} NO esta en la lista.')