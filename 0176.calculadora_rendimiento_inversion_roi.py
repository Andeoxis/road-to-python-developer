def calcular_roi(ganancia_obtenida, costo_inversion):
    """Calculadora de Retorno sobre la Inversion (ROI) y beneficio neto"""
    beneficio_neto = ganancia_obtenida - costo_inversion
    roi_porcentaje = (beneficio_neto / costo_inversion) * 100
    return beneficio_neto, roi_porcentaje


print(f"\n{calcular_roi.__doc__}")

while True:
    try:
        costo = float(input("Monto invertido inicialmente ($): "))
        if costo <= 0:
            raise ValueError

        retorno = float(input("Ingreso total generado ($): "))
        if retorno < 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: El costo debe ser mayor a cero y el retorno no puede ser negativo.\n")

neto, roi = calcular_roi(retorno, costo)
print("\nMetricas de rendimiento:")
print(f"- Beneficio neto: ${neto:.2f}")
print(f"- Retorno (ROI):  {roi:.2f}%")