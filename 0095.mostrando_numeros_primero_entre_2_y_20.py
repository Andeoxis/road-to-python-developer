inicio_rango = 2
fin_rango = 20

print(f"Números primos entre {inicio_rango} y {fin_rango}:")
for num in range(inicio_rango, fin_rango + 1):
    if num > 1: # Los números primos deben ser mayores que 1
        es_primo = True
        # Comprobamos divisores desde 2 hasta la raíz cuadrada de num
        # (o hasta num-1, pero la raíz cuadrada es más eficiente)
        # Podemos iterar hasta int(num**0.5) + 1
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0: # Si es divisible, no es primo
                es_primo = False
                break # No necesitamos seguir comprobando
        if es_primo:
            print(num)