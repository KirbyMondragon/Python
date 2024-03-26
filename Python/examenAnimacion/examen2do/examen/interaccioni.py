import numpy as np

def obtener_valor(numero):
    while True:
        try:
            valor = float(input(f"Ingrese el valor {numero} para la matriz: "))
            return valor
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

def obtener_dimension(numero):
    while True:
        try:
            valor = int(input(f"Ingrese la dimensión {numero} para la matriz: "))
            return valor
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para la dimensión.")

def llenar_matriz_3d(depth, rows, cols):
    matriz = np.zeros((depth, rows, cols))  # Inicializar matriz con ceros
    for i in range(depth):
        print(f"\nCapa {i + 1}:")
        for j in range(rows):
            for k in range(cols):
                valor = obtener_valor(f"[{i + 1}, {j + 1}, {k + 1}]")
                matriz[i, j, k] = valor
                print(f"Matriz actual:\n{matriz}")  # Mostrar matriz actual
    return matriz

def suma_matrices_3d(matriz_a, matriz_b):
    return matriz_a + matriz_b

def resta_matrices_3d(matriz_a, matriz_b):
    return matriz_a - matriz_b

def multiplicacion_matrices_3d(matriz_a, matriz_b):
    return matriz_a * matriz_b

while True:
    try:
        # Obtener dimensiones de las matrices
        depth = obtener_dimension("de profundidad")
        rows = obtener_dimension("de filas")
        cols = obtener_dimension("de columnas")

        # Llenar matrices tridimensionales
        print("Llenado de Matriz A:")
        matriz_A = llenar_matriz_3d(depth, rows, cols)

        print("\nLlenado de Matriz B:")
        matriz_B = llenar_matriz_3d(depth, rows, cols)

        # Mostrar resultados
        print("\nMatriz A:")
        print(matriz_A)
        print("\nMatriz B:")
        print(matriz_B)

        while True:
            try:
                # Menú de opciones para operaciones
                print("\n¿Qué operación desea realizar?")
                print("1. Suma de matrices")
                print("2. Resta de matrices")
                print("3. Multiplicación de matrices")
                print("4. Reiniciar y llenar con nuevos datos")
                print("5. Salir")

                opcion = int(input("Ingrese el número de la operación deseada: "))

                if opcion == 1:
                    resultado = suma_matrices_3d(matriz_A, matriz_B)
                    print("\nResultado de la suma:")
                    print(resultado)
                elif opcion == 2:
                    resultado = resta_matrices_3d(matriz_A, matriz_B)
                    print("\nResultado de la resta:")
                    print(resultado)
                elif opcion == 3:
                    resultado = multiplicacion_matrices_3d(matriz_A, matriz_B)
                    print("\nResultado de la multiplicación:")
                    print(resultado)
                elif opcion == 4:
                    break  # Salir del bucle y reiniciar el programa
                elif opcion == 5:
                    print("Saliendo del programa. ¡Hasta luego!")
                    quit()
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
            except ValueError:
                print("Por favor, ingrese un número válido para la opción del menú.")
    except KeyboardInterrupt:
        print("\n¡Ha ocurrido un error! Asegúrate de ingresar valores numéricos para las dimensiones.")
