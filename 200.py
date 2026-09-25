lista = []
while True:
    try:
        for i in range(1,6):
            edad = int(input('Ingrese su edad: '))
            if edad <= 0 or edad >= 100:
                raise ValueError
            lista.append(edad)
        break
    except ValueError:
        print('Dato erroneo.')
        print('Intente nuevamente.')

print(f'Esta es la lista de las edades: {lista}')
suma = sum(lista)
promedio = suma / 5
print(f'el promedio de las edades es: {promedio}')