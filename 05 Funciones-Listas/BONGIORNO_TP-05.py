#ejercicio 1

lista_numeros = list(range(4,101,4))
print(lista_numeros)

#ejercicio 2

lista = ["cocina","sarten","cuchillo","batidor","olla"]
penultimo_elemento = lista[3]

print(penultimo_elemento)

#ejercicio 3

lista_vacia = []

lista_vacia.append("piano")
lista_vacia.append(45)
lista_vacia.append(True)

print(lista_vacia)

#ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]

animales [1] = "loro"
animales [3] = "oso"

print(animales)

#ejercicio 5

numeros = [8, 15, 3, 22, 7] 
numeros.remove(max(numeros))
print(numeros)

#lo que se sucede aquí es que elimina el valor más alto dentro de la lista 'numeros' (en este caso el 22)

#ejercicio 6

numeros = list(range(10,31,5))

dos_primeros = numeros[0:2]

print(dos_primeros)

#ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "amarok"
autos[2] = "up"

print(autos)

#ejercicio 8

dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#ejercicio 10

lista_anidada = [15, True,[25.5, 57.9, 30.6], False]

print(lista_anidada)