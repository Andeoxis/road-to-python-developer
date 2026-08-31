def calculador(dato1, dato2, operacion):
    match operacion:
        case '+':
            return dato1 + dato2
        case '-':
            return dato1 - dato2
        case '*':
            return dato1 * dato2
        case '/':
            return dato1 / dato2
    
dato1 = int(input('Ingrese el dato1 : '))
dato2 = int(input('Ingrese el dato2 : '))
operacion = input('Ingrese la operacion a realizar: ')

respuesta_total = calculador(dato1, dato2, operacion)     
print(f'La respuesta es: {dato1} {operacion} {dato2} = {respuesta_total}')   