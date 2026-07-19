def controlar_ventilacion(temperatura_actual):
    if temperatura_actual <= 30:
        return 'Apagado'
    elif 30 < temperatura_actual <= 45:
        return 'Ventilacion Baja'
    
    return 'ALERTA: Ventilacion Maxima'

ingreso_de_temperatura_actual = float(input('Ingrese la temperatura actual: '))
estado_ventilador = controlar_ventilacion(ingreso_de_temperatura_actual)
print(f'El estado del ventilador es: {estado_ventilador}')
    