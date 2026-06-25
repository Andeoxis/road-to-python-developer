# Imagina que estás mejorando el sistema de tu negocio de pollos.
# Vas a crear un script para despachar pedidos al por mayor.
# El programa debe pedir dos datos obligatorios y no continuará hasta que ambos estén perfectos:

# El tipo de producto: Solo aceptamos "pollo" o "huevo".

# La cantidad de cajas: Para que valga la pena el envío, la cantidad debe estar entre 10 y 50 cajas.

# Si el usuario se equivoca en el producto O se equivoca en la cantidad, el programa lo reiniciará por completo.

# Instrucciones para tu archivo 026.despacho_pedidos.py:

# Afuera del bucle: Pide los dos datos:

# Python
# producto = input("Ingrese el producto (pollo / huevo): ").lower().strip()
# cantidad = int(input("Ingrese la cantidad de cajas (10 a 50): "))
# La condición del while (El Gran Candado):
# Queremos que el bucle se repita mientras el producto esté MAL, O BIEN la cantidad esté MAL.

# ¿Cómo sabemos si el producto está mal? Cuando producto != 'pollo' and producto != 'huevo'

# ¿Cómo sabemos si la cantidad está mal? Cuando not (10 <= cantidad <= 50)

# ¿Cómo los unimos? Con un or en el medio.

# Pista de oro: ```python
# while (producto != 'pollo' and producto != 'huevo') or not (10 <= cantidad <= 50):

# Adentro del bucle:

# Imprime: "Uno o ambos datos son incorrectos. Verifique el catálogo e intente de nuevo."

# Vuelve a pedir ambos datos (producto y cantidad) para que el usuario pueda corregirlos.

# Afuera del bucle: Si logra salir, significa que todo está impecable. Imprime:

# f"Pedido confirmado: Despachando {cantidad} cajas de {producto}. ¡Buen viaje! 🚚"

producto = input('Ingrese el producto (pollo / huevo): ')
cantidad = int(input('Ingrese la cantidad de cajas (10 a 50):'))
while (producto != 'pollo' and producto != 'huevo') or not (10 < cantidad < 50):
    print('Uno o mas datos son incorrectos. Verifique el catalogo e intente de nuevo')
    producto = input('Ingrese el producto (pollo / huevo): ')
    cantidad = int(input('Ingrese la cantidad de cajas (10 a 50):'))
print(f'Pedido confirmado: Despachando {cantidad} cajas de {producto}. Buen viaje')