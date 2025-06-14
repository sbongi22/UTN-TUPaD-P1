#ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

#ejercicio 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

#ejercicio 3

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#ejercicio 4

contactos = {}
for i in range(1,6):
    nombre = input(f"Nombre del contacto n°{i}: ")
    numero = input(f"Número telefónico n°{i}: ")
    contactos[nombre] = numero

consulta = input("Consultar número de: ")
print(contactos[consulta])

#ejercicio 5

frase = input("Ingrese una frase: ").split()

palabras_unicas = set(frase)
recuento = {palabra: frase.count(palabra) for palabra in palabras_unicas}

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

#ejercicio 6

alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Nota {i+1}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    print(f"{nombre}: Promedio = {sum(notas)/3:.2f}")

#ejercicio 7

parcial1 = {"Ana", "Luis", "María"}
parcial2 = {"Juan", "María", "Jorge"}

ambos_parciales = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos_parciales)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#ejercicio 8

stock = {"Lapiz": 50, "Cuaderno": 20}

producto = input("Coloque un producto a consultar stock o quiera agregar: ")
if producto in stock:
    print(f"Stock: {stock[producto]}")
    stock[producto] += int(input("Unidades a agregar: "))
else:
    stock[producto] = int(input("Nuevo producto, coloque stock correspondiente: "))

print(stock)

#ejercicio 9

agenda = {("lunes", "10:00"): "Reunión", ("martes", "15:00"): "Clase de inglés"}

dia, hora = input("Ingrese día y hora para conocer la actividad: ").split()
print(agenda.get((dia, hora), "No hay evento"))

#ejercicio 10

listado = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertir = {capital: pais for pais, capital in listado.items()}
print(invertir)
