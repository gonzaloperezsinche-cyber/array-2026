notas = [15, 18, 12, 17, 20]

# Función para imprimir notas
def imprimir_notas(notas):
    for nota in notas:
        print(nota)

# Función para calcular el promedio
def calcular_promedio(lista_notas):
    suma = 0
    for nota in lista_notas:
        suma += nota
    return suma / len(lista_notas)

# Función para calcular la nota mayor
def calcular_nota_mayor(notas):
    mayor = notas[0]
    for i in range(1, len(notas)):
        if notas[i] > mayor:
            mayor = notas[i]
    return mayor

# Función para calcular la nota menor
def calcular_nota_menor(notas):
    menor = notas[0]
    for i in range(1, len(notas)):
        if notas[i] < menor:
            menor = notas[i]
    return menor

# Imprimir las notas
imprimir_notas(notas)

# Calcular e imprimir el promedio de las notas
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")

# Calcular e imprimir la nota mayor y menor
mayor = calcular_nota_mayor(notas)
menor = calcular_nota_menor(notas)
print(f"La nota mayor es: {mayor}")
print(f"La nota menor es: {menor}")