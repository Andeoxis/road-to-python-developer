# Variables globales con memoria a largo plazo
correcto = 0
incorrecto = 0
suma_de_todos_los_pollos = 0

for i in range(1, 5):
    peso = float(input(f'Ingrese el peso del pollo N {i}: '))
    
    # Filtro de Seguridad: El peso debe ser físicamente real
    if 0 < peso < 5:
        correcto += 1
        suma_de_todos_los_pollos += peso
        print('✅ Dato registrado correctamente.')
    else:
        incorrecto += 1
        print(f'🚨 ERROR. El peso {peso}kg es imposible. Registro descartado.')
    print()

print(f'📊 --- REPORTE DE CALIDAD DE DATOS ---')
print(f'🟢 Registros válidos: {correcto}')
print(f'🔴 Registros inválidos: {incorrecto}')

# La forma más óptima: Una sola división al final de todo
if correcto > 0:
    promedio = suma_de_todos_los_pollos / correcto
    print(f'⚖️ El peso promedio real (sin errores) es de: {promedio:.2f} kilos, papuchin.')
else:
    print('❌ No se ingresó ningún dato válido hoy para calcular un promedio.')