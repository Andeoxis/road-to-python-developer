def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Imprimir los primeros 10 números de Fibonacci usando el generador
for number in fibonacci_generator(10):
    print(number)