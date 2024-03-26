import numpy as np

# Definimos matrices
A = np.array([[[24, 10, 57, 63], [41, 80, 70, 88], [61, 46, 44, 10]],
              [[74, 26, 11, 97], [20, 6, 11, 5], [67, 51, 58, 90]]])

B = np.array([[[15, 30, 45, 3], [85, 2, 1, 16], [10, 9, 14, 22]],
              [[5, 28, 67, 17], [16, 44, 78, 39], [13, 60, 37, 5]]])

C = np.zeros_like(A)

print("Tu matriz A es:")
print(A)
print()
print("Tu matriz B es:")
print(B)
print()

m = A.shape[0]
r = A.shape[1]
f = A.shape[2]

profundidad = 0

while profundidad < m:
    filas = 0
    while filas < r:
        columnas = 0
        while columnas < f:
            C[profundidad, filas, columnas] = A[profundidad, filas, columnas] + B[profundidad, filas, columnas]
            columnas += 1
        filas += 1
    profundidad += 1

print("La suma de tus matrices es:")
print(C)
