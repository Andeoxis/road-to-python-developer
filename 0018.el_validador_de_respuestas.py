# Imagina que estás cobrando en tu negocio y le preguntas al cliente si quiere factura.
# Solo te puede responder "si" o "no". Si escribe cualquier otra tontería,
# el programa se lo va a volver a preguntar infinitamente hasta que ponga una respuesta válida.

# Instrucciones:

# Pide la respuesta por primera vez afuera y antes del bucle:

# Python
# respuesta = input("¿Desea factura? (si / no): ").lower().strip()
# Crea el while con esta condición: Mientras la respuesta NO sea igual a 'si' Y TAMBIÉN la respuesta NO sea igual a 'no'.

# Pista en Python: while respuesta != 'si' and respuesta != 'no':

# Adentro del bucle (significa que el usuario se equivocó):

# Imprime un mensaje: "Respuesta no válida, gil."

# Vuelve a pedir el input dentro del bucle guardándolo en la misma variable: respuesta =
# input(...) (Si no vuelves a pedir el input adentro, la variable nunca cambia y el bucle se vuelve infinito).

# Afuera del bucle, imprime: "Perfecto, procesando tu solicitud...".

respuesta = input('Quiere factura? (si / no) ').lower().strip()
while respuesta != 'si' and respuesta != 'no':
    print('Respuesta no valida, intente de nuevo')

    respuesta = input('Quiere factura? (si / no) ').lower().strip()

if respuesta == 'si':
    print('perfecto, aca esta su factura')
else:
    print('Perfecto, entonces sin factura sera, gracias')