import numpy as np  # Importa la librería numpy bajo el alias np

# Funciones de la calculadora básica
def calculadora_basica():
    while True:
        try:
            resultado = int(input("Ingrese el número 1: "))  # Solicita al usuario ingresar el primer número
            while True:  # Bucle para operaciones continuas
                num = int(input("Ingrese el número 2: "))  # Solicita al usuario ingresar el segundo número
                print("Calculadora Basica")
                print("  ")
                print("Operaciones disponibles:")
                print("1. Suma")
                print("2. Resta")
                print("3. Multiplicación")
                print("4. División")
                print("5. Salir de la Calculadora Básica")
                operacion = int(input("Ingrese el número de operacion: "))  # Solicita al usuario ingresar el número de operación
                
                # Realiza la operación correspondiente según la opción seleccionada por el usuario
                if operacion == 1:
                    resultado += num
                    print("Resultado actual:", resultado)
                elif operacion == 2:
                    resultado -= num
                    print("Resultado actual:", resultado)
                elif operacion == 3:
                    resultado *= num
                    print("Resultado actual:", resultado)
                elif operacion == 4:
                    if num != 0:
                        resultado /= num
                        print("  ")
                        print("Resultado actual: ", resultado)
                    else:
                        print("No es posible dividir por cero")
                elif operacion == 5:
                    print("Saliendo de la Calculadora Básica.")
                    return  # Sale de la función de la calculadora básica
                else:
                    print("Opción no válida")

        except ValueError:
            print("Por favor, ingrese un número válido.")

# Funciones de la calculadora de matrices
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
    matriz = np.zeros((depth, rows, cols))  # Inicializa una matriz con ceros utilizando la librería numpy
    for i in range(depth):
        print(f"\nCapa {i + 1}:")
        for j in range(rows):
            for k in range(cols):
                valor = obtener_valor(f"[{i + 1}, {j + 1}, {k + 1}]")  # Solicita al usuario ingresar valores para la matriz
                matriz[i, j, k] = valor  # Asigna el valor a la posición correspondiente en la matriz
                print(f"Matriz actual:\n{matriz}")  # Muestra la matriz actual
    return matriz

def suma_matrices_3d(matriz_a, matriz_b):
    return matriz_a + matriz_b  # Realiza la suma de matrices

def resta_matrices_3d(matriz_a, matriz_b):
    return matriz_a - matriz_b  # Realiza la resta de matrices

def multiplicacion_matrices_3d(matriz_a, matriz_b):
    return matriz_a * matriz_b  # Realiza la multiplicación de matrices

# Menú principal
while True:  # Bucle que asegura que el menú se mantenga disponible hasta que el usuario decida salir
    print("Bienvenidos a la UPSRJ, ¿Tacos doña tifo?")  # Muestra un mensaje de bienvenida

    try:
        print("Menu principal")  # Muestra el encabezado del menú principal
        print("1. Calculadora Básica")
        print("2. Calculadora de Matrices")
        print("3. Salir")

        opcion_principal = input("Ingrese el número de la opción deseada: ")  # Solicita al usuario elegir una opción del menú

        if opcion_principal == "1":
            calculadora_basica()  # Invoca la función de la calculadora básica si se elige la opción 1
        elif opcion_principal == "2":
            print("Calculadora de Matrices")  # Muestra la etiqueta de la calculadora de matrices

            while True:  # Bucle para operaciones continuas con matrices
                try:
                    depth = obtener_dimension("de profundidad")  # Obtiene la dimensión de profundidad de la matriz
                    rows = obtener_dimension("de filas")  # Obtiene la dimensión de filas de la matriz
                    cols = obtener_dimension("de columnas")  # Obtiene la dimensión de columnas de la matriz

                    print("Llenado de Matriz A:")
                    matriz_A = llenar_matriz_3d(depth, rows, cols)  # Llena la Matriz A con valores ingresados por el usuario

                    print("\nLlenado de Matriz B:")
                    matriz_B = llenar_matriz_3d(depth, rows, cols)  # Llena la Matriz B con valores ingresados por el usuario

                    print("\nMatriz A:")
                    print(matriz_A)  # Muestra la Matriz A ingresada por el usuario
                    print("\nMatriz B:")
                    print(matriz_B)  # Muestra la Matriz B ingresada por el usuario

                    while True:  # Bucle para las operaciones con matrices
                        try:
                            print("\n¿Qué operación desea realizar?")
                            print("1. Suma de matrices")
                            print("2. Resta de matrices")
                            print("3. Multiplicación de matrices")
                            print("4. Agregar nuevos datos")
                            print("5. Salir")

                            opcion_matrices = int(input("Ingrese el número de la operación deseada: "))

                            if opcion_matrices == 1:
                                resultado = suma_matrices_3d(matriz_A, matriz_B)
                                print("\nResultado de la suma:")
                                print(resultado)
                            elif opcion_matrices == 2:
                                resultado = resta_matrices_3d(matriz_A, matriz_B)
                                print("\nResultado de la resta:")
                                print(resultado)
                            elif opcion_matrices == 3:
                                resultado = multiplicacion_matrices_3d(matriz_A, matriz_B)
                                print("\nResultado de la multiplicación:")
                                print(resultado)
                            elif opcion_matrices == 4:
                                break  # Sale del bucle actual para agregar nuevos datos a las matrices
                            elif opcion_matrices == 5:
                                print("Saliendo del programa. ¡Hasta luego!")
                                quit()  # Finaliza el programa si se elige la opción 5
                            else:
                                print("Opción no válida. Por favor, seleccione una opción válida.")
                        except ValueError:
                            print("Por favor, ingrese un número válido para la opción del menú.")

                except KeyboardInterrupt:
                    print("\n¡Ha ocurrido un error! Asegúrate de ingresar valores numéricos para las dimensiones.")

        elif opcion_principal == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break  # Sale del bucle principal y termina el programa si se elige la opción 3
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    except KeyboardInterrupt:
        print("\nHa ocurrido un error. Intente nuevamente.")

