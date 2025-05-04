# main.py

from gestor import GestorTareas

def mostrar_menu():
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    gestor = GestorTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción: ")
            gestor.agregar_tarea(nombre, descripcion)
        elif opcion == '2':
            gestor.mostrar_tareas()
        elif opcion == '3':
            gestor.mostrar_tareas()
            indice = int(input("Número de la tarea a marcar como completada: ")) - 1
            if not gestor.marcar_completada(indice):
                print("Índice inválido.")
        elif opcion == '4':
            gestor.mostrar_tareas()
            indice = int(input("Número de la tarea a eliminar: ")) - 1
            if not gestor.eliminar_tarea(indice):
                print("Índice inválido.")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
