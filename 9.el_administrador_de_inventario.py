# Vas a programar un sistema para controlar el stock de una tienda. El inventario comenzará con 10 productos disponibles. El usuario podrá decidir si quiere vender productos, reponer productos o cerrar el sistema.

# Instrucciones paso a paso:

# Crea una variable llamada stock con el valor de 10 afuera y antes de iniciar tu while True (para que no se reinicie en cada vuelta).

# Inicia tu bucle while True.

# Adentro del bucle, muestra un mensaje que le diga al usuario cuántas unidades hay (ej. f'Stock actual: {stock} unidades').

# Pide al usuario que elija una acción con un input() que diga: "¿Qué desea hacer? (vender / reponer / salir): ".

# Evalúa la opción con condiciones:

# Si escribe "vender": Pídele al usuario cuántas unidades quiere vender (usa int(input(...))).

# Condición interna: Si la cantidad a vender es menor o igual al stock actual, restas esa cantidad al stock (stock = stock - cantidad) y muestras un mensaje: "Venta exitosa.".

# Si no: Muestras un error: "No hay suficiente stock disponible." (y no restas nada).

# Si escribe "reponer": Pídele al usuario cuántas unidades están llegando, súmalas al stock (stock = stock + cantidad) y muestra un mensaje: "Stock actualizado.".

# Si escribe "salir": Muestra un mensaje de despedida y usa el break para terminar el programa.

# Si escribe cualquier otra cosa: Muestra un mensaje que diga "Opción no válida. Intente de nuevo.".

stock = 10
while True:
    print(f'Stock actual {stock} unidades')
    accion = input('Que desea hacer? (vender / reponer / salir): ').lower().strip()
    if accion == 'vender':
        cantidad = (int(input('Cuantas unidades quiere vender: ')))
        if cantidad <= stock:
            stock -= cantidad
            print('Stock actualizado.')
        else:
            print('No hay sufuciente stock disponible')
    elif accion == 'reponer':
        unidades_llegadas = int(input('Cuantas unidades estan llegando dime: '))
        stock += unidades_llegadas
        print('Stock actualizado.')
    elif accion == 'salir':
        print('Un gusto poder ayudarlo')
        break
    else:
        print('Opcion no valida. Intente de nuevo')



            
        