notas = [15, 18, 12, 17, 20]
# Función imprimir notas
def ImprimirNotas(notas):
    for nota in notas:
        print(nota)

# Imprimir las notas
ImprimirNotas(notas)


# Calcular el promedio de las notas usando una función

def CalcularPromedio(lista_notas):
    suma = 0
    for nota in lista_notas:
        suma += nota
    promedio = suma / len(lista_notas)
    print(f"El promedio es: {promedio}")

CalcularPromedio(notas)