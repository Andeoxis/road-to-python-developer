correcto = 0
incorrecto = 0
suma_de_todos_los_pollos = 0
for i in range(1, 5):
    peso = float(input(f'\nIngrese el peso del pollo N {i}: '))
    if 0 < peso < 5:
        correcto += 1
        suma_de_todos_los_pollos += peso
        promedio = suma_de_todos_los_pollos / correcto
        print('Dato registrado correctamente')
    else:
        incorrecto += 1
        print(f'ERROR. El peso {peso}kg es imposible. Registro descartado.')
    print()
print(f'Registros validos son: {correcto}')
print(f'Registros invalidos son: {incorrecto}')
print(f'El peso promedio real (sin errores) es de: {promedio:.2f} kilos, papuchin.')
