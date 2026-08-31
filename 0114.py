def filtrar_precios_altos(lista_precios, limite):
    precios_filtrados = []

    for precio in lista_precios:
        if precio > limite:
            precios_filtrados.append(precio)
    return precios_filtrados

precios_inventario = [90, 100, 80, 10, 20]
limite_de_busqueda = 50

resultado = filtrar_precios_altos(precios_inventario, limite_de_busqueda)
print(f'Los precios mayores a {limite_de_busqueda}Bs son {resultado}')
        