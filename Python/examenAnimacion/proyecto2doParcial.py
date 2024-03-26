import datetime

tareas = []

def agregar_tarea():
    # Se solicita al usuario que ingrese el nombre de la tarea.
    nombre = input("Ingrese el nombre de la tarea: ")

    while True:
        # Se pide al usuario que ingrese la fecha límite para la tarea.
        fecha_limite = input("Ingrese la fecha límite (DD/MM/AAAA): ")
        formato_correcto = False

        try:
            # Se intenta convertir la entrada del usuario a un objeto datetime.
            fecha_limite = datetime.datetime.strptime(fecha_limite, "%d/%m/%Y")
            # Se verifica si la fecha límite es igual o mayor que la fecha actual.
            if fecha_limite.date() >= datetime.datetime.now().date():
                formato_correcto = True  # El formato y la fecha son válidos.
            else:
                print("La fecha límite debe ser igual o mayor a la fecha de hoy.")
        except ValueError:
            # Se imprime un mensaje si el formato de fecha ingresado es incorrecto.
            print("Formato de fecha incorrecto. Intente de nuevo (DD/MM/AAAA)")
            print("Recuerde que su tarea tiene que ser para el día de hoy o en el futuro.")

        if formato_correcto:
            break  # Sale del bucle si el formato y la fecha son válidos.

    # Se solicita al usuario que ingrese la prioridad de la tarea.
    prioridad = input("Ingrese la prioridad (alta, media, baja): ")

    # Se registra la fecha de creación de la tarea.
    fecha_creacion = datetime.datetime.now()

    # Se crea una lista con los detalles de la tarea y se agrega a la lista de tareas.
    tarea = [nombre, fecha_limite.strftime("%d/%m/%Y"), prioridad, fecha_creacion]
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

# Resto del código sin comentarios, manteniendo la funcionalidad anterior...

def programa_principal():
    # Función principal que controla el menú y las opciones del gestor de tareas.
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
