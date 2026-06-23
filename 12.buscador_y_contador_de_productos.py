# Imagina que tu lista de compras ya es gigante y a veces repites productos sin querer
# (por ejemplo, agregas 'huevos' tres veces en diferentes momentos). Vamos a crear un menú interactivo para analizar tu lista.

# Instrucciones:

# Crea una lista ya inicializada con algunos elementos repetidos afuera del bucle para no tener que escribirlos cada vez.
# Copia esta línea tal cual antes de tu while True:

# Python
# lista_compras = ['huevos', 'leche', 'huevos', 'pan', 'huevos', 'leche']
# Inicia tu bucle while True.

# Pide al usuario que elija una opción limpia con .strip().lower(): (ver / buscar / total / salir).

# Evalúa las opciones:

# Si escribe "ver": Muestra la lista completa.

# Si escribe "buscar": Pídele al usuario qué producto quiere buscar (ej. 'huevos').
# Luego, usa .count() para saber cuántas veces está. Ejemplo de uso: cantidad = lista_compras.count(producto_buscado).

# Si la cantidad es mayor a 0, muestra: f"El producto '{producto_buscado}' se repite {cantidad} veces."

# Si es 0, muestra: "Ese producto no está en la lista."

# Si escribe "total": Muestra cuántos productos hay en total acumulados en la lista usando len(lista_compras).

# Si escribe "salir": Rompe el bucle con break.

lista_compras = ['huevos', 'leche', 'huevos', 'pan', 'huevos', 'leche']
while True:
    opcion_limpia = input('Elija alguna de las opciones. (ver / buscar / total / salir).')
    if opcion_limpia == 'ver':
        print(f'Tu lista es esta {lista_compras}')
    elif opcion_limpia == 'buscar':
        opcion_a_buscar = input('Que producto desea buscar: ')
        cantidad = lista_compras.count(opcion_a_buscar)
        if cantidad > 0:
            print(f'Hay un total de {cantidad} de producto {opcion_a_buscar}')
        else:
            print('Ese producto no esta en la lista')
    elif opcion_limpia == 'total':
        print(f'Tines un total de {len(lista_compras)}.')
    elif opcion_limpia == 'salir':
        print('Hasta luego')
        break

    


            
