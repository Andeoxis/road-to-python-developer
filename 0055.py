# Lista de precios actuales de producción
precios_actuales = [15.50, 22.00, 18.30, 35.00, 12.00]
precios_con_inflacion = []

print("🚀 --- PROCESANDO AJUSTE DE PRECIOS ---")

# El 'for' recorre cada precio de la lista automáticamente
for precio in precios_actuales:
    nuevo_precio = precio * 1.085  # Aumento del 8.5%
    precios_con_inflacion.append(nuevo_precio)
    print(f"💰 Precio antiguo: {precio:.2f} Bs. -> Nuevo precio: {nuevo_precio:.2f} Bs.")

print("\n✅ Proceso completado. Precios actualizados en la base de datos.")