# Vamos a simular una app de notas donde puedas ir armando tu lista de compras para el supermercado.
# Aquí vas a aprender a usar una Lista ([]) y su función .append() para meter elementos dentro de ella.

# Instrucciones:

# Crea una lista vacía llamada lista_compras = [] afuera y antes de tu while True.

# Inicia tu bucle while True.

# Pide al usuario que elija una opción: "¿Qué desea hacer? (agregar / ver / salir): ".
# No olvides limpiarlo con .strip().lower().

# Evalúa las opciones:

# Si escribe "agregar": Pídele al usuario el nombre del producto (ej. "¿Qué producto deseas agregar?: "). Luego, agrega ese producto a tu lista usando: lista_compras.append(producto). Muestra un mensaje confirmando que se agregó.

# Si escribe "ver": * Condición interna: Si la lista está vacía, muestra un mensaje: "Tu lista está vacía.".

# Si no: Muestra la lista en pantalla usando un simple print(f"Tu lista actual es: {lista_compras}").

# Si escribe "salir": Muestra la lista final, despídete y usa break.

# Cualquier otra cosa: "Opción no válida."

lista_compras = []
while True:
    accion = input('Que desea hacer? (agregar / ver / salir ) ').lower().strip()
    if accion == 'agregar':
        que_agregara = input('Que producto deseas agregar? ').lower().strip()
        lista_compras.append(que_agregara)
        print(f'Se agrego {que_agregara} a la lista')
    elif accion == 'ver':
        if lista_compras == []:
            print('Tu lista esta vacia')
            print('Intente de nuevo')
        else:
            print(f'Tu lista actual es : {lista_compras}')
    elif accion == 'salir':
        print(f'Tu lista final es {lista_compras}.')
        break
    else:
        print('Opcion no valida')
        print('Intente de nuevo gil')
