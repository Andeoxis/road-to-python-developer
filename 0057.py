CLAVE_CORRECTA = "AsusStrix2026"

print("🔒 --- SISTEMA DE SEGURIDAD BIOMÉTRICO ---")

for intento in range(1, 4):
    print(f"Intento {intento} de 3")
    password = input("Ingrese su contraseña de administrador: ")
    
    if password == CLAVE_CORRECTA:
        print("🔓 ACCESO CONCEDIDO. Bienvenido al servidor central, jefe.")
        break  # Rompe el bucle de inmediato porque ya no necesitamos más intentos
    else:
        print("❌ Contraseña incorrecta.")
        print()
else:
    # El 'else' de un 'for' solo se ejecuta si el bucle terminó los 3 intentos sin tocar un 'break'
    print("🚨 SISTEMA BLOQUEADO. Se ha enviado una alerta al administrador.")