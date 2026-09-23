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

# Imprimir la nota mayor y menor

minimo = notas[0]
maximo = notas[0]
 
for i in range(1, len(notas)):
 
    if notas[i] < minimo:
        minimo = notas[i]
 
    if notas[i] > maximo:
        maximo = notas[i]
 
 
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")