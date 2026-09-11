def calcular_proporcion_porcentual(parte, total):
    """Calculadora de representacion porcentual y razon fraccionaria"""
    porcentaje = (parte / total) * 100
    razon = parte / total
    return porcentaje, razon


print(f"\n{calcular_proporcion_porcentual.__doc__}")

while True:
    try:
        total = float(input("Ingrese el total o muestra completa: "))
        if total <= 0:
            raise ValueError

        parte = float(input("Ingrese la parte o subconjunto: "))
        if parte < 0 or parte > total:
            raise ValueError

        break
    except ValueError:
        print("ERROR: El total debe ser positivo y la parte no puede exceder al total.\n")

pct, proporcion = calcular_proporcion_porcentual(parte, total)
print("\nAnalisis proporcional:")
print(f"- Representacion porcentual: {pct:.2f}%")
print(f"- Factor decimal (razon):   {proporcion:.4f}")