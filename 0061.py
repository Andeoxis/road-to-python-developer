# Rendimiento real medido en porcentaje de 5 lotes (el estándar mínimo aceptable es 85%)
rendimiento_lotes = [92.4, 78.1, 88.5, 65.0, 90.2]
C_COSTO_LOTE_FALLIDO = 3500  # Cuánto dinero cuesta en Bs. si un lote rinde mal

lotes_eficientes = 0
lotes_defectuosos = 0
perdida_total = 0

print("🔬 --- AUDITORÍA AUTOMATIZADA DE EFICIENCIA ---")

# El 'for' examina el porcentaje de cada lote uno por uno
for i, rendimiento in enumerate(rendimiento_lotes, start=1):
    if rendimiento >= 85.0:
        lotes_eficientes += 1
        print(f"🟢 Lote N {i}: Rendimiento del {rendimiento}% -> ✅ APROBADO")
    else:
        lotes_defectuosos += 1
        perdida_total += C_COSTO_LOTE_FALLIDO
        print(f"🔴 Lote N {i}: Rendimiento del {rendimiento}% -> ⚠️ RECHAZADO (Bajo el estándar)")

print("\n📊 --- REPORTE GLOBAL DE PRODUCTIVIDAD ---")
print(f"✅ Total lotes óptimos: {lotes_eficientes}")
print(f"❌ Total lotes con pérdidas: {lotes_defectuosos}")
print(f"💸 Pérdida económica total estimada: {perdida_total:.2f} Bs.")