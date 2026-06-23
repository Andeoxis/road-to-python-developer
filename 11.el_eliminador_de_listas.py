# Vamos a usar el mismo código de la lista de compras que ya tienes hecho,
# pero le vamos a añadir una nueva opción para subir el nivel: la opción de "eliminar" un producto si nos arrepentimos.

# Tu reto es agregar un nuevo elif que haga lo siguiente:

# En la pregunta principal, añade la opción en el texto: (agregar / ver / eliminar / salir).

# Crea un nuevo bloque: elif accion == 'eliminar':.

# Adentro de ese bloque, pídele al usuario qué producto quiere borrar:
# producto_a_borrar = input('¿Qué producto deseas eliminar?: ').lower().strip()

# Condición interna (¡Pista clave!): Antes de borrarlo,
#                    debes revisar si ese producto realmente existe en la lista. En Python se hace usando la palabra clave in.

# Si el producto está en la lista: Usas la función .remove() para sacarlo, por ejemplo:
# lista_compras.remove(producto_a_borrar). Y muestras un mensaje de "Producto eliminado".

# Si el producto NO está en la lista: Muestras un mensaje que diga "Ese producto no está en tu lista".

lista_compras = []
while True:
    accion = input('Que desea hacer? (agregar / ver / eliminar / salir) ').lower().strip()
    
    if accion == 'agregar':
        que_agregara = input('Que producto deseas agregar? ').lower().strip()
        lista_compras.append(que_agregara)
        print(f'Se agrego {que_agregara} a la lista')
        
    elif accion == 'ver': # CAMBIADO A ELIF
        if lista_compras == []:
            print('Tu lista esta vacia')
        else:
            print(f'Tu lista actual es : {lista_compras}')

    elif accion == 'eliminar':
        producto_a_borrar = input('Que producto deseas eliminar? ').lower().strip()
        if producto_a_borrar in lista_compras:
            lista_compras.remove(producto_a_borrar)
            print('Producto eliminado')
        else:
            print('Ese producto no esta en tu lista')

        
    elif accion == 'salir': # CAMBIADO A ELIF
        print(f'Tu lista final es {lista_compras}.')
        break
        
    else: # Ahora este else SOLO responde si no se cumplió NINGUNO de los de arriba
        print('Opcion no valida')
        print('Intente de nuevo gil')