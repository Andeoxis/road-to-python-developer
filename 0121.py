dato = int(input('Ingresa del 1 al 10 hasta que numero de la tabla quisieras ver: '))
if dato < 0:
    print('ERROR')
else:
    for dato in range(1,dato, + 1):
        for j in range(1,11):
            print(f'{dato} * {j} = {dato * j}')
        print()