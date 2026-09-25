lista = []
for i in range(1, 6):
    numero_ingresado = int(input(f'Ingrese el numero {i}: '))
    lista.append(numero_ingresado)

print(lista)
suma = sum(lista)
print(suma)
