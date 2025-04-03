#TP 1 - Santiago Bongiorno - Comisión 10

#ejercicio 1
print("Hola Mundo!")

#ejercicio 2
nombre = input("Coloque su nombre:")
print(f"Hola {nombre}!")

#ejercicio 3
nombre = input("Coloque su nombre:")
apellido = input("Coloque su apellido:")
edad = input("Coloque su edad:")
lugar = input("Coloque su lugar de residencia:")
print(f"Soy {nombre}, tengo {edad} años y vivo en {lugar}")

#ejercicio 4
pi = float(3.14)
radio = float(input("Coloque el radio de un círculo:"))
perimetro = 2 * pi * radio
area = pi * radio ** 2

print(f"El área es del círculo es {area} y su perímetro {perimetro}")

#ejercicio 5
seg = int(input("Coloque una cantidad de segundos:"))
horas = seg / 3600

print(f"{seg} segundos equivale a {horas} horas")

#ejercicio 6
numero = int(input("Coloque un número:"))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#ejercicio 7
num1 = int(input("Coloque un primer número distinto a 0:"))
num2 = int(input("Coloque un segundo número distinto a 0:"))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

#ejercicio 8
peso = float(input("Coloque su peso en kg:"))
altura = float(input("Coloque su altura en metros:"))
imc = peso / (altura ** 2)

print(f"Su índice de masa corporal es {imc}")

#ejercicio 9
temp = float(input("Coloque la temperatura en °C:"))
fahr = 9/5 * temp + 32

print(f"La temperatura en Fahrenheit es de {fahr} °F")

#ejercicio 10
num1 = int(input("Coloque un primer número:"))
num2 = int(input("Coloque un segundo número:"))
num3 = int(input("Coloque un tercer número:"))
promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los números colocados es {promedio}")