# Puedes empezar definiendo N aquí
N = 5

# Tu código para calcular la suma de los primeros N números pares
lista = []
for numeros in range(1, 9):
  if numeros % 2 == 0:
    print(numeros)
    lista.append(numeros)
    suma = sum(lista)
print(f'Sumando toda lista me da un resultado de: {suma}')