# 1. Menú interactivo
print("--- SISTEMA DE PEAJE ---")
print("1: Auto")
print("2: Moto")
print("3: Camión")

opcion = input("Seleccione el tipo de vehículo (1-3): ")

tarifa_base = 0
vehiculo = ""

# Uso de match/case (Switch/Case en Python)
match opcion:
    case "1":
        vehiculo = "Auto"
        tarifa_base = 50.0  # Tarifas de ejemplo (puedes cambiarlas)
    case "2":
        vehiculo = "Moto"
        tarifa_base = 20.0
    case "3":
        vehiculo = "Camión"
        tarifa_base = 100.0
    case _:
        print("Opción no válida.")
        exit()

# 2 y 3. Verificación de hora pico con condicionales anidadas
es_hora_pico_input = input("¿Es hora pico? (si/no): ").lower().strip()

tarifa_final = tarifa_base

if es_hora_pico_input == "si":
    # Condicional anidada para calcular el recargo del 15%
    recargo = tarifa_base * 0.15
    tarifa_final = tarifa_base + recargo
    print(f"\nSe aplicó un recargo de hora pico (15%): ${recargo:.2f}")
else:
    if es_hora_pico_input == "no":
        print("\nNo aplica recargo de hora pico.")
    else:
        print("\nEntrada no válida para hora pico, se mantendrá tarifa base.")

# Resumen de cobro
print("\n" + "="*30)
print(f"Vehículo: {vehiculo}")
print(f"Tarifa Base: ${tarifa_base:.2f}")
print(f"Total a pagar: ${tarifa_final:.2f}")
print("="*30)

# Sello de avance al finalizar la ejecución
print("[SELLO DE AVANCE]: Ejercicio procesado e impreso con éxito.")