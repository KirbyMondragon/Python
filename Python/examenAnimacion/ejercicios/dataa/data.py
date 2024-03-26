import numpy as np

# Generamos matrices aleatorias con la misma forma que las originales A y B
matriz_1 = np.random.randint(0, 100, size=(2, 3, 4))
matriz_2 = np.random.randint(0, 100, size=(2, 3, 4))
resultado = np.zeros_like(matriz_1)

print("Tu nueva matriz 'matriz_1' es:")
print(matriz_1)
print()
print("Tu nueva matriz 'matriz_2' es:")
print(matriz_2)
print()

m = matriz_1.shape[0]
r = matriz_1.shape[1]
f = matriz_1.shape[2]

profundidad = 0

while profundidad < m:
    filas = 0
    while filas < r:
        columnas = 0
        while columnas < f:
            resultado[profundidad, filas, columnas] = matriz_1[profundidad, filas, columnas] + matriz_2[profundidad, filas, columnas]
            columnas += 1
        filas += 1
    profundidad += 1

print("La suma de tus nuevas matrices es:")
print(resultado)