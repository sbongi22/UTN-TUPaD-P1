#ejercicio 1

for i in range(0,101):
    print(i)

#ejercicio 2

num = input("Ingrese un número entero: ")
cantidad_digitos = len(num)

print("El número tiene", cantidad_digitos, "dígito(s)")

#ejercicio 3

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un segundo número entero: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 + 1, num2):
    suma += i

print("La suma de los números entre", num1, "y", num2, "es:", suma)

#ejercicio 4

num = int(input("Ingrese un número entero: "))
parar_suma = 0
suma = 0

while num != parar_suma:
    suma = suma + num
    num = int(input("Ingrese otro número entero: "))

print("La suma total de números es: ", suma)

#ejercicio 5

import random
numero_aleatorio = random.randint(0, 9)

intentos = 0
adivinanza = -1

while adivinanza != numero_aleatorio:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

print("Bien! Lo adivinaste en", intentos, "intento(s)" )

#ejercicio 6

for i in range(100, -1, -1):
    print(i)

#ejercicio 7

num = int(input("Ingresa un número entero positivo: "))

if num < 0:
    print("El número debe ser positivo")
else:
    suma = 0
    for i in range(0, num + 1):
        suma += i

    print("La suma de los números de 0 a", num, "es:", suma)

#ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingresa 100 números enteros:")

for i in range(100):
    numero = int(input(f"Ingresá el número #{i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Ingresó", pares, "números pares,", impares, "números impares,", positivos, "positivos y", negativos, "negativos")

#ejercicio 9

print("Ingresa 100 números enteros:")

suma_total = 0
for i in range(100):
    numero = int(input(f"Ingresá el número #{i+1}: "))
    suma_total += numero

media = suma_total / 100

print("La media de los 100 números ingresados es", media)

#ejercicio 10

numero = input("Ingresa un número: ")

if numero.startswith("-"):
    numero_invertido = "-" + numero[:0:-1]
else:
    numero_invertido = numero[::-1]

print("El número invertido es", numero_invertido)
