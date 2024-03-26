import pandas as pd
import datetime

# Crear un DataFrame vacío para almacenar las tareas
columnas = ['Nombre', 'Fecha límite', 'Prioridad', 'Fecha de creación', 'Etiquetas', 'Categoría']
tareas_df = pd.DataFrame(columns=columnas)

def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")

    while True:
        fecha_limite = input("Ingrese la fecha límite (DD/MM/AAAA): ")
        formato_correcto = False

        try:
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
    etiquetas = input("Ingrese etiquetas para la tarea separadas por coma (ej. Trabajo, Urgente): ").split(',')
    categoria = input("Ingrese la categoría para la tarea: ")

    fecha_creacion = datetime.datetime.now()

    # Crear listas para etiquetas y categorías, simular arreglos multidimensionales
    etiquetas_2d = [etiquetas]
    categorias_3d = [[[nombre, fecha_limite.strftime("%d/%m/%Y"), prioridad]]]

    # Agregar la tarea al DataFrame
    nueva_tarea = pd.DataFrame([[nombre, fecha_limite.strftime("%d/%m/%Y"), prioridad, fecha_creacion, etiquetas_2d, categorias_3d]], columns=columnas)
    global tareas_df
    tareas_df = tareas_df.append(nueva_tarea, ignore_index=True)
    print("Tarea agregada con éxito.")

def mostrar_tareas():
    if tareas_df.empty:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for idx, tarea in tareas_df.iterrows():
            print(f"{idx+1}. Nombre: {tarea['Nombre']}, Fecha límite: {tarea['Fecha límite']}, Prioridad: {tarea['Prioridad']}, Fecha de creación: {tarea['Fecha de creación']}")
            print(f"   Etiquetas: {', '.join(tarea['Etiquetas'][0])}")

# Aquí podrías definir funciones para eliminar, editar, etc.

def programa_principal():
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            mostrar_tareas()
        elif opcion == '3':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    programa_principal()
