def calcular_triple(numero_a_calcular):
    resultado = numero_a_calcular * 3
    return resultado

numero_ingresado = int(input(f'Ingrese un numero: '))
el_triple = calcular_triple(numero_ingresado)
print(f'El triple del numero ingresado es: {el_triple}')