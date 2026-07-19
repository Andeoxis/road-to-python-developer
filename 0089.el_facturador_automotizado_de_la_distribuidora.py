def calcular_tota_venta(cantidad, producto):
    producto_limpio = producto.lower().strip()
    
    if producto_limpio == 'pollo':
        precio_base = cantidad * 16
        if cantidad > 10:
            return precio_base - 15
        return precio_base # Si es 10 o menos, paga normal
        
    elif producto_limpio == 'huevo':
        precio_base = cantidad * 28
        if cantidad > 5:
            return precio_base - 10
        return precio_base # Si es 5 o menos, paga normal
        
    return 'Producto no disponible'

# --- PROGRAMA PRINCIPAL ---
insertar_producto = input('Ingrese el producto (pollo/huevo): ')
insertar_cantidad = int(input('Ingrese cantidad: '))

# CORRECCIÓN: Pasamos primero la CANTIDAD y luego el PRODUCTO, tal como lo definiste arriba
precio_final = calcular_tota_venta(insertar_cantidad, insertar_producto)

if precio_final == 'Producto no disponible':
    print('ERROR: Producto seleccionado erroneamente.')
else:
    print(f'El precio total a pagar es: {precio_final} Bs')