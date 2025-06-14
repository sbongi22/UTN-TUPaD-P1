#ejercicio 1

def factorial(n):

    if n == 0:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(max_num):
    for i in range(1, max_num + 1):
        print(f"{i} = {factorial(i)}")

numero = int(input("Ingrese un número entero positivo: "))
if numero >= 1:
    mostrar_factoriales(numero)
else:
    print("Error. El número debe ser positivo")

#ejercicio 2

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)

num = int(input("Ingrese el número hasta qué posición desea ver en la serie de Fibonacci: "))

if num >= 0:
    for i in range(num + 1):
        fibo = fibonacci(i)
        print(f"{i} = {fibo}")
else:
    print("Error. El número debe ser positivo")

#ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if exponente >= 0:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")
else:
    print("Error. El exponente debe ser positivo")

#ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero positivo: "))

if num >= 0:
    binario = decimal_a_binario(num)
    print(f"El número {num} en binario es: {binario}")
else:
    print("Error. El número debe ser positivo")

#ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra: ")
resultado = es_palindromo(palabra)
print(f"{resultado}")

#ejercicio 6

def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)

num = int(input("Ingrese un número positivo: "))
resultado = suma_digitos(num)
print(f"{resultado}")

#ejercicio 7

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)

num = int(input("Ingrese el número de bloques del nivel inferior: "))
resultado = contar_bloques(num)
print(f"Se necesitan {resultado} bloques para completar la pirámide")

#ejercicio 8

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    ultimo = numero % 10
    resto = numero // 10
    return (1 if ultimo == digito else 0) + contar_digito(resto, digito)

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese un dígito positivo: "))

if dig >= 0 and dig <= 9:
    if num >= 0:
        resultado = contar_digito(num, dig)
        print(f"El dígito {dig} está {resultado} veces en {num}")
    else:
        print("Error. El número debe ser positivo")
else:
    print("Error. El dígito debe ser positivo")