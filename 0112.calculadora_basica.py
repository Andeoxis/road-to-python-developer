def operar(a, b, operador):
    match operador:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b <= 0:
                return 'Error. No se puede division entre cero.'
            return a / b
        case _:
            return 'Error. Dato erroneo.'
            


dato1 = int(input('Ingrese dato 1:\n'))
dato2 = int(input('Ingrese dato 2:\n'))
operadorr = input('Ingrese la operacion a realizar (+, -, *, /)\n')

respuesta_total = operar(dato1, dato2, operadorr)
print(f'Se hara lo siguiente: {dato1} {operadorr} {dato2} = {respuesta_total}')