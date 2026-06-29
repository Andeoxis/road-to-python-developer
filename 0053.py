normal = 0
anomalia = 0

for i in range(1, 5):
    peso = float(input(f'Ingrese el peso del pollo N {i}: '))
    
    # Capa 1: Filtro Externo (Seguridad de datos)
    if 0 < peso < 5:
        
        # Capa 2: Filtro Interno Anidado (Clasificación de Inteligencia de Datos)
        if 2.8 <= peso <= 3.5:
            normal += 1
            print('✅ Peso dentro del estándar.')
        else:
            anomalia += 1
            print(f'⚠️ ALERTA: Anomalía detectada en el pollo N {i}.')
            
    else:
        print(f'🚨 ERROR: El peso {peso}kg es imposible. Registro descartado.')
    print()
     
print(f'''📊 --- REPORTE DE CONTROL DE ANOMALÍAS ---
🟢 Total aves en rango normal: {normal}
🟡 Total anomalías críticas: {anomalia}''')