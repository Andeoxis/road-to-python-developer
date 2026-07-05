comentarios = [
    "El pedido llegó a tiempo y todo muy fresco",
    "🚨 ALERTA: El camión de distribución se retrasó y los huevos se pueden arruinar",
    "Quiero cotizar 500 pollos para el próximo mes",
    "🚨 ALERTA: La balanza digital de la sucursal norte está dando error de pesaje"
]

alertas_detectadas = 0

print("🔍 --- ESCANEANDO MENSAJES DEL SISTEMA ---")

for mensaje in comentarios:
    # Si la palabra 'ALERTA' está dentro del texto...
    if "ALERTA" in mensaje:
        alertas_detectadas += 1
        print(f"⚠️ NOTIFICACIÓN CRÍTICA ENCONTRADA: {mensaje}")

print(f"\n📊 Reporte: Se encontraron {alertas_detectadas} problemas urgentes hoy.")