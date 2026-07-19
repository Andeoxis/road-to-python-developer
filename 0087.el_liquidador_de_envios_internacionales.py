def calcular_costo_de_envio(peso_paquete, destino):
    costo_base = peso_paquete * 15
    
    # 1. Caso Nacional (Con los paréntesis correctos en .lower())
    if destino.lower() == 'nacional':
        return costo_base
        
    # 2. Caso Internacional Ligero (Usamos elif en vez de anidar)
    elif peso_paquete < 5:
        return costo_base + 50
        
    # 3. Caso Internacional Pesado (Cualquier otra opción cae aquí)
    return costo_base + 120

# --- PROGRAMA PRINCIPAL ---
peso_insertado = float(input('Ingrese el peso de la maleta (kg): '))
destino_insertado = input('Ingrese el destino (Nacional / Internacional): ')

costo_final = calcular_costo_de_envio(peso_insertado, destino_insertado)

print('\n----- REPORTE DE ENVÍO -----')
print(f'El costo final es de: {costo_final:.2f} Bs.')