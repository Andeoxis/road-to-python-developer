# 1. LA FUNCIÓN SE QUEDA EXACTAMENTE IGUAL (Impecable)
def operar(a, b, operador):
    match operador:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return 'Error. No se puede dividir entre cero.'
            return a / b
        case _:
            return 'Error. Dato erróneo.'


# 2. CÓDIGO PRINCIPAL CON BUCLE CONTINUO
while True:
    print("\n--- NUEVA OPERACIÓN ---")
    
    dato1 = int(input('Ingrese dato 1:\n'))
    dato2 = int(input('Ingrese dato 2:\n'))
    operadorr = input('Ingrese la operación a realizar (+, -, *, /):\n')

    respuesta_total = operar(dato1, dato2, operadorr)
    print(f'Resultado: {dato1} {operadorr} {dato2} = {respuesta_total}')

