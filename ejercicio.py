notas = [15, 18, 12, 17, 20]
# Función imprimir notas
def ImprimirNotas(notas):
    for nota in notas:
        print(nota)

# Imprimir las notas
ImprimirNotas(notas)


# Calcular el promedio de las notas
cantidad_notas = len(notas)
suma = 0
promedio = 0
for nota in notas:
    suma += nota

promedio = suma / cantidad_notas