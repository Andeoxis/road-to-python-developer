suma_notas = 0
promedio = 0
for i in range(1, 5):
    while True:
        try:
            notas = int(input('Ingresa tus notas:\n'))
            suma_notas += notas
            break
        except ValueError:
            print('ERROR: Los datos que colocaste son incorrectos, intente de nuevo')

promedio = suma_notas / 4
if promedio >= 51:
    print(f'Felicidades aprobaste con {promedio}/100.')
else:
    print(f'Reprobaste... Tu nota es de {promedio}/100.')
print(f'Tu promedio es de {promedio}')
