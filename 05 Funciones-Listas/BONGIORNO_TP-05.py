#ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#ejercicio 2

def saludar_usuario(nombre_ingresado):
    print(f"Hola {nombre_ingresado}!")

# Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su ciudad de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#ejercicio 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = int(input("Ingrese el radio de un círculo para calcular su área y perímetro: "))

print(f"El área del círculo es {calcular_area_circulo(radio):.2f} y su perímetro es {calcular_perimetro_circulo(radio):.2f}")

#ejercicio 5

def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingresa una cantida de segundos que desea pasar a horas: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas")

#ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Coloque un número: "))
tabla_multiplicar(numero)

#ejercicio 7

def operaciones_basicas(a, b):
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")

# Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

operaciones_basicas(num1, num2)

#ejercicio 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

print(f"Su IMC es de {calcular_imc(peso, altura):.2f}")

#ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingrese la temperatura en C°: "))
print(f"La temperatura en F° es de {celsius_a_fahrenheit(celsius):.2f}")

#ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio entre {num1}, {num2} y {num3} es {promedio:.2f}")