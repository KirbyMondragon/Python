import datetime

# Lista para almacenar las tareas
tareas = []

# Matriz para almacenar las etiquetas de cada tarea
etiquetas_tareas = []

# Matriz para almacenar las categorías y las tareas en cada categoría
categorias_tareas = []

def agregar_tarea():
    # Solicitar nombre, fecha límite y prioridad para la tarea
    nombre = input("Ingrese el nombre de la tarea: ")

    while True:
        fecha_limite = input("Ingrese la fecha límite (DD/MM/AAAA): ")
        formato_correcto = False

        try:
            # Validar el formato de la fecha límite
            fecha_limite = datetime.datetime.strptime(fecha_limite, "%d/%m/%Y")
            if fecha_limite.date() >= datetime.datetime.now().date():
                formato_correcto = True
            else:
                print("La fecha límite debe ser igual o mayor a la fecha de hoy.")
        except ValueError:
            print("Formato de fecha incorrecto. Intente de nuevo (DD/MM/AAAA)")
            print("Recuerde que su tarea tiene que ser para el día de hoy o en el futuro.")
        
        if formato_correcto:
            break

    prioridad = input("Ingrese la prioridad (alta, media, baja): ")

    # Solicitar y almacenar etiquetas para la tarea
    etiquetas = input("Ingrese etiquetas para la tarea separadas por coma (ej. Trabajo, Urgente): ").split(',')
    etiquetas_tareas.append(etiquetas)

    # Solicitar y almacenar categoría para la tarea
    categoria = input("Ingrese la categoría para la tarea: ")
    tareas_categoria = [nombre, fecha_limite.strftime("%d/%m/%Y"), prioridad]
    categorias_tareas.append([categoria, [tareas_categoria]])

    fecha_creacion = datetime.datetime.now()

    # Agregar la tarea a la lista principal de tareas
    tarea = [nombre, fecha_limite.strftime("%d/%m/%Y"), prioridad, fecha_creacion]
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

# Función para mostrar todas las tareas con sus etiquetas
def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for idx, tarea in enumerate(tareas, start=1):
            print(f"{idx}. Nombre: {tarea[0]}, Fecha límite: {tarea[1]}, Prioridad: {tarea[2]}, Fecha de creación: {tarea[3]}")
            print(f"   Etiquetas: {', '.join(etiquetas_tareas[idx - 1])}")

# Función para eliminar una tarea seleccionada por el usuario
def eliminar_tarea():
    # Mostrar todas las tareas disponibles para eliminar
    mostrar_tareas()
    if not tareas:
        print("No hay tareas para eliminar.")
        return

    indice = int(input("Ingrese el número de la tarea que desea eliminar: "))
    if 1 <= indice <= len(tareas):
        # Eliminar la tarea seleccionada junto con sus etiquetas y categorías correspondientes
        tarea_eliminada = tareas.pop(indice - 1)
        etiquetas_tareas.pop(indice - 1)
        categorias_tareas.pop(indice - 1)
        print(f"Tarea '{tarea_eliminada[0]}' eliminada correctamente.")
    else:
        print("Índice de tarea inválido.")

# Función para editar una tarea seleccionada por el usuario
def editar_tarea():
    mostrar_tareas()
    if not tareas:
        print("No hay tareas para editar.")
        return

    indice = int(input("Ingrese el número de la tarea que desea editar: "))
    if 1 <= indice <= len(tareas):
        tarea = tareas[indice - 1]

        # Solicitar y actualizar nombre, fecha límite y prioridad para la tarea
        nombre = input(f"Ingrese el nuevo nombre para '{tarea[0]}': ")
        fecha_limite = input(f"Ingrese la nueva fecha límite para '{tarea[1]}': ")
        prioridad = input(f"Ingrese la nueva prioridad para '{tarea[2]}': ")

        tarea[0] = nombre
        tarea[1] = fecha_limite
        tarea[2] = prioridad

        # Editar también las etiquetas y categorías correspondientes
        etiquetas = input("Ingrese etiquetas actualizadas para la tarea separadas por coma: ").split(',')
        etiquetas_tareas[indice - 1] = etiquetas

        categoria = input("Ingrese la nueva categoría para la tarea: ")
        categorias_tareas[indice - 1][0] = categoria

        print("Tarea editada correctamente.")
    else:
        print("Índice de tarea inválido.")

# Función principal que controla el menú y las opciones del gestor de tareas
def programa_principal():
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Editar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            mostrar_tareas()
        elif opcion == '3':
            eliminar_tarea()
        elif opcion == '4':
            editar_tarea()
        elif opcion == '5':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    programa_principal()
