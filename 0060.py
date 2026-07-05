# Listas ordenadas por tipo de producto (Pollo Entero, Pechuga, Alitas, Huevos)
inventario_manana = [100, 150, 80, 300]
unidades_vendidas = [45, 120, 80, 210]
productos = ["Pollo Entero", "Pechuga Filet", "Alitas", "Maples de Huevo"]

print("📦 --- BALANCE DIARIO DE INVENTARIO AUTOMÁTICO ---")

# 'zip' junta las tres listas y el 'for' las procesa en parejas exactas
for prod, stock_inicial, venta in zip(productos, inventario_manana, unidades_vendidas):
    stock_final = stock_inicial - venta
    
    print(f"🔹 {prod}:")
    print(f"   Inició con: {stock_inicial} unid. | Se vendieron: {venta} unid.")
    print(f"   库存 Stock actual en almacén: {stock_final} unidades.")
    
    # Alerta crítica si nos quedamos sin stock para el día siguiente
    if stock_final == 0:
        print("   🚨 ALERTA: ¡Producto agotado! Es necesario reponer urgente.")
    print()

print("✅ Conciliación de inventario completada con éxito.")