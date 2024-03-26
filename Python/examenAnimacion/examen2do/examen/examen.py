import numpy as np

def suma_matrices_3d(matriz_a, matriz_b):
    return matriz_a + matriz_b

def resta_matrices_3d(matriz_a, matriz_b):
    return matriz_a - matriz_b

def multiplicacion_matrices_3d(matriz_a, matriz_b):
    return matriz_a * matriz_b

# Ejemplo de matrices tridimensionales
matriz_A = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
matriz_B = np.array([[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]])

# Operaciones con las matrices tridimensionales
resultado_suma = suma_matrices_3d(matriz_A, matriz_B)
resultado_resta = resta_matrices_3d(matriz_A, matriz_B)
resultado_multiplicacion = multiplicacion_matrices_3d(matriz_A, matriz_B)

# Mostrar resultados
print("Matriz A:")
print(matriz_A)
print("\nMatriz B:")
print(matriz_B)
print("\nResultado de la suma:")
print(resultado_suma)
print("\nResultado de la resta:")
print(resultado_resta)
print("\nResultado de la multiplicación:")
print(resultado_multiplicacion)
