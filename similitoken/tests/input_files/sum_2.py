# Este módulo está diseñado para ofrecer funciones que calculen estadísticas descriptivas

from statistics import mean, median, multimode

def obtener_promedio(valores):
    # Devuelve el promedio aritmético de una secuencia numérica
    if not valores:
        raise ValueError("La lista no puede estar vacía")
    return mean(valores)

def obtener_mediana(valores):
    # Calcula el valor medio de una secuencia numérica
    if not valores:
        raise ValueError("La lista no puede estar vacía")
    return median(valores)

def obtener_modas(valores):
    # Encuentra los valores más frecuentes en una secuencia numérica
    if not valores:
        raise ValueError("La lista no puede estar vacía")
    return multimode(valores)

# Secuencia de entrada para el cálculo de estadísticas
secuencia = [5, 1, 3, 3, 2, 1, 4, 2, 5, 5, 1]

# Visualización de las estadísticas descriptivas
print(f"Promedio: {obtener_promedio(secuencia)}")
print(f"Mediana: {obtener_mediana(secuencia)}")
print(f"Modas: {obtener_modas(secuencia)}")
