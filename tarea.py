class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True
