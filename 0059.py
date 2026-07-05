# Lista de temperaturas del sensor. Los ceros son errores de conexión
lecturas_sensor = [24.5, 0.0, 25.1, 24.8, 0.0, 26.2, -1.0, 23.9]
lecturas_limpias = []

print("🌡️ --- INICIANDO DEPURACIÓN DE SENSORES IOT ---")

for temperatura in lecturas_sensor:
    # Si la lectura es menor o igual a cero, es un error del sensor
    if temperatura <= 0:
        print("⚠️ Salto de registro: Detectado error de lectura o sensor desconectado.")
        continue  # Salta directo a la siguiente vuelta del for, ignorando lo que sigue abajo
        
    # Si el dato es bueno, se guarda
    lecturas_limpias.append(temperatura)

print("\n📊 --- DATASET LIMPIO PARA MODELO DE IA ---")
print(f"Datos originales: {lecturas_sensor}")
print(f"Datos listos para la IA: {lecturas_limpias}")