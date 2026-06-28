mayor_peso = 0
id_del_pollo = 0
for numero_de_pollos in range(1, 6):
    peso = float(input(f'Ingresa el peso del pollo N {numero_de_pollos}: '))
    if mayor_peso < peso:
        mayor_peso = peso
        id_del_pollo = numero_de_pollos
        print(f'✨ ¡Pollo N° {numero_de_pollos} toma la delantera con {peso} kilos!')
    print()
Costo_total_de_la_prodruccion_de_esta_produccion = 14 * numero_de_pollos
print(f'El pollo campeon es el pollo N {id_del_pollo} con un peso de: {mayor_peso}.')
print(f'El costo total de la produccion de las {numero_de_pollos} aves fue de: {Costo_total_de_la_prodruccion_de_esta_produccion}Bs.')