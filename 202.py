lista = []
while True:
    try:
        lista.clear()
        print('\n---- BIENVENIDO AL SISTEMA DE CONTEO ----\n')
        for i in range(1, 7):
            ingreso_numero = input('Ingrese algun producto para agregar: ')
            if ingreso_numero.isdigit():
                raise ValueError
            if ingreso_numero in lista:
                raise ValueError
            lista.append(ingreso_numero)
        print(f'Esta es tu lista: {lista}')
        break
    except ValueError:
        print('ERROR. Intente nuevamente.')

while True:
    try:
        buscado = input('Ingrese el producto a buscar: ')
        encontrado = False
        posicion = 0
        if buscado not in lista:
            raise ValueError
        for e in range(len(lista)):
            if lista[e] == buscado:
                encontrado = True
                posicion = e
                break
        break
    except ValueError:
        print('ERROR.')
    
if encontrado:
    print(f'El producto {buscado} se encuentra en el indice {posicion}.')
else:
    print(f'El numero {buscado} NO esta en la lista.')
    