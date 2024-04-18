# Este script calcula estadísticas básicas para una lista de números

import statistics

def calcular_promedio(numeros):
    # Retorna el promedio de una lista de números
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    # Retorna la mediana de una lista de números
    return statistics.median(numeros)

def calcular_moda(numeros):
    # Retorna la moda de una lista de números
    return statistics.mode(numeros)

# Lista de números para análisis
datos = [4, 1, 3, 2, 4, 4, 5, 3, 3, 3, 2]

# Cálculo y despliegue de estadísticas
print(f"Promedio: {calcular_promedio(datos)}")
print(f"Mediana: {calcular_mediana(datos)}")
print(f"Moda: {calcular_moda(datos)}")
