# gestor.py

from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion):
        tarea = Tarea(nombre, descripcion)
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            return True
        return False

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            return True
        return False
