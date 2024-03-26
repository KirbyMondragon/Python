import numpy as np

# Crear un inventario de ropa como una matriz de dos arreglos de tres dimensiones
# Dimensiones: [Tipo de prenda][Color][Talla]
inventario_ropa = np.zeros((3, 4, 5), dtype=int)  # Por ejemplo: 3 tipos, 4 colores, 5 tallas

# Función para agregar productos al inventario de ropa
def agregar_producto(tipo_prenda, color, talla, cantidad, sucursal):
    inventario_ropa[tipo_prenda][color][talla] += cantidad
    print(f"Se agregaron {cantidad} unidades de {tipo_prenda} - Color: {color} - Talla: {talla} en la sucursal {sucursal}.")

# Función para mostrar el inventario de ropa
def mostrar_inventario():
    print("Inventario de ropa:")
    for tipo_prenda, tipo_array in enumerate(inventario_ropa):
        for color, color_array in enumerate(tipo_array):
            for talla, cantidad in enumerate(color_array):
                if cantidad > 0:
                    print(f"Tipo: {tipo_prenda}, Color: {color}, Talla: {talla}, Cantidad: {cantidad}")

# Ejemplo de uso:
agregar_producto(0, 1, 2, 10, "Sucursal A")  # Por ejemplo: Pantalón, Color: Azul, Talla: M, 10 unidades
agregar_producto(1, 2, 3, 5, "Sucursal B")   # Por ejemplo: Camisa, Color: Rojo, Talla: XL, 5 unidades

mostrar_inventario()
