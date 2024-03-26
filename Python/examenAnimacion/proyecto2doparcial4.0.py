import numpy as np

# Función para agregar un nuevo producto al inventario de una dimensión
def agregar_producto(nombre, precio, cantidad, inventario):
    nuevo_producto = np.array([nombre, precio, cantidad])
    inventario = np.vstack([inventario, nuevo_producto])
    return inventario

# Función para mostrar el inventario de una dimensión
def mostrar_inventario(inventario):
    print("Inventario:")
    for producto in inventario:
        print(f"Nombre: {producto[0]}, Precio: ${producto[1]}, Cantidad: {producto[2]}")

# Función para agregar descripción y proveedor al inventario de dos dimensiones
def agregar_detalles(descripcion, proveedor, inventario):
    detalles = np.array([[descripcion, proveedor]])

    if inventario.size == 0:
        inventario = detalles
    else:
        if len(inventario) == len(detalles):
            inventario = np.hstack([inventario, detalles.T])
        else:
            print("Las dimensiones no coinciden. No se pueden agregar los detalles.")

    return inventario

# Función para mostrar el inventario detallado de dos dimensiones
def mostrar_inventario_detallado(inventario):
    print("Inventario Detallado:")
    for producto in inventario:
        print(f"Nombre: {producto[0]}, Precio: ${producto[1]}, Cantidad: {producto[2]}, "
              f"Descripción: {producto[3]}, Proveedor: {producto[4]}")

# Ejemplo de uso:
# Crear inventario de una dimensión
inventario_1d = np.array([
    ["Producto 1", 10.99, 50],
    ["Producto 2", 5.99, 100],
    ["Producto 3", 20.50, 30]
])

# Agregar un nuevo producto al inventario de una dimensión
inventario_1d = agregar_producto("Producto 4", 15.00, 75, inventario_1d)
mostrar_inventario(inventario_1d)

# Crear inventario detallado de dos dimensiones
inventario_2d = np.array([
    ["Producto 1", 10.99, 50, "Descripción 1", "Proveedor A"],
    ["Producto 2", 5.99, 100, "Descripción 2", "Proveedor B"],
    ["Producto 3", 20.50, 30, "Descripción 3", "Proveedor C"]
])

# Agregar detalles al inventario detallado de dos dimensiones
inventario_2d = agregar_detalles("Nueva Descripción", "Nuevo Proveedor", inventario_2d)
mostrar_inventario_detallado(inventario_2d)
