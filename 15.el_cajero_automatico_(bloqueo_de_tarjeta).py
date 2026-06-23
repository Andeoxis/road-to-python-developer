# Imagina que estás programando el software de un cajero automático.
# El usuario mete su tarjeta y tiene que ingresar su PIN secreto.
# Si se equivoca 3 veces, el cajero bloquea la tarjeta por seguridad y corta el programa inmediatamente,
# sin darle más opciones.

# El PIN correcto va a ser 5555 (un número entero).

# Instrucciones:

# Crea la variable intentos_pin = 3 afuera y antes del while True.

# Inicia tu bucle while True.

# Pide al usuario que ingrese su PIN: pin_ingresado = int(input("Ingrese su PIN de 4 dígitos: "))

# Evalúa las condiciones en el orden correcto:

# Si el PIN es correcto (== 5555): Muestras un mensaje de éxito:
# "¡PIN correcto! Retirando dinero..." y usas un break para terminar de forma exitosa.

# Si falló (cualquier otro número): Lo primero que haces es restarle un intento: intentos_pin = intentos_pin - 1.

# Inmediatamente revisas si se quedó sin intentos: Si intentos_pin == 0, muestras el mensaje de error definitivo:
# "Tarjeta bloqueada por seguridad. Acuda a su banco." y tiras un break para cerrar el juego.

# Si todavía le quedan intentos: Le adviertes cuántos le quedan: f"PIN incorrecto. Te quedan {intentos_pin} intentos."