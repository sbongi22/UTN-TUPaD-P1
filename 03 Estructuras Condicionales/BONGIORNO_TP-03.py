#ejercicio 1

edad = int(input("Coloque su edad: "))

if (edad >= 18):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#ejercicio 2

nota = int(input("Coloque la nota del examen: "))

if (nota >= 6 and nota <= 10):
    print("Aprobado")
elif (nota < 6 and nota > 0):
    print("Desaprobado")
else:
    print("Coloque una nota correcta")

#ejercicio 3

numero = int(input("Coloque un número par: "))

if (numero % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#ejercicio 4

edad = int(input("Coloque su edad: "))

if (edad < 12 and edad >= 0):
    print("Categoría: Niño")
elif (edad >= 12 and edad < 18):
    print("Categoría: Adolescente")
elif (edad >= 18 and edad < 30):
    print("Categoría: Adulto/a joven")
elif (edad >= 30):
    print("Categoría: Adulto/a")
else:
    print("Ingresó una edad incorrecta")

#ejercicio 5

contraseña = input("Coloque una contraseña entre 8 y 14 caracteres: ")

if (8 <= len(contraseña) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(10)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Números:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if (media > mediana > moda):
    print("Sesgo positivo (a la derecha)")
elif (media < mediana < moda):
    print("Sesgo negativo (a la izquierda)")
elif (media == mediana == moda):
    print("Sin sesgo")
else:
    print("No se cumple ningún sesgo definido")

#ejercicio 7

texto = input("Coloque una frase o palabra: ")

if texto[-1] in 'aeiou':
    texto += "!"
    
print(texto)

#ejercicio 8

nombre = input("Coloque su nombre: ")
formato = input("Indique con número: 1. Mayúscula - 2. Minúscula - 3. Primera letra mayúscula: ")

if (formato == "1"):
    print(nombre.upper())
elif (formato == "2"):
    print(nombre.lower())
elif (formato == "3"):
    print(nombre.capitalize())
else:
    print("Coloque un número válido")

#ejercicio 9

terremoto = int(input("Coloque la magnitud del terremoto en la escala de Richter: "))

if (terremoto < 3 and terremoto > 0):
    print("'Muy leve' (imperceptible)")
elif (terremoto >= 3 and terremoto < 4):
    print("'Leve' (ligeramente perceptible)")
elif (terremoto >= 4 and terremoto < 5):
    print("'Moderado' (sentido por personas, pero generalmente no causa daños)")
elif (terremoto >= 5 and terremoto < 6):
    print("'Fuerte' (puede causar daños en estructuras débiles)")
elif (terremoto >= 6 and terremoto < 7):
    print("'Muy Fuerte' (puede causar daños significativos)")    
elif (terremoto >= 7):
    print("'Extremo' (puede causar graves daños a gran escala)")
else:
    print("Ingrese una magnitud correcta")

#ejercicio 10

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio no válido"

print("Usted se encuentra en la estación", estacion)