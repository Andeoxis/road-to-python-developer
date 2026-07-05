# Ventas diarias en unidades de 5 puntos de venta
ventas_sucursales = [12, 25, 18, 30, 15]
numero_sucursal = 1

print("📊 --- VISUALIZACIÓN DE VENTAS DIARIAS ---")

for venta in ventas_sucursales:
    # Multiplicamos el string '*' por el número de ventas para crear una barra visual
    barra_grafica = "◼️" * venta
    print(f"Sucursal N {numero_sucursal}: {barra_grafica} ({venta} unidades)")
    numero_sucursal += 1

print("\nAnálisis visual generado correctamente.")