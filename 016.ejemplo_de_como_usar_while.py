# 1. Creamos una variable para llevar la cuenta
contador = 1

# 2. El bucle evalúa: ¿El contador es menor o igual a 5?
while contador <= 5:
    print(f"Vuelta número: {contador}")
    
    # 3. ¡VITAL! Le sumamos 1 al contador para que cambie en la siguiente vuelta
    contador = contador + 1

print("El bucle terminó porque contador llegó a 6.")