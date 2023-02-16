class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cantidad_tareas = 0
    
    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea, self.primero)
        self.primero = nuevo_nodo
        if self.ultimo is None:
            self.ultimo = nuevo_nodo
        self.cantidad_tareas += 1
    
    def eliminar_ultima_tarea(self):
        if self.ultimo is None:
            print("El historial de tareas está vacío.")
        elif self.primero == self.ultimo:
            tarea_eliminada = self.ultimo.dato
            self.primero = None
            self.ultimo = None
            self.cantidad_tareas = 0
            print("Se eliminó la tarea de tareas pendientes.")
        else:
            actual = self.primero
            while actual.siguiente != self.ultimo:
                actual = actual.siguiente
            tarea_eliminada = self.ultimo.dato
            actual.siguiente = None
            self.ultimo = actual
            self.cantidad_tareas -= 1
            print("Se eliminó la tareadel historial de tareas pendientes.")
    
    def mostrar_todas_las_tareas(self):
        if self.primero is None:
            print("El historial de tareas pendientes está vacío.")
        else:
            actual = self.primero
            tareas = []
            while actual is not None:
                tareas.append(actual.dato)
                actual = actual.siguiente
            print("Historial de tareas pendientes (en orden inverso):")
            for tarea in reversed(tareas):
                print(tarea)
    
    def mostrar_cantidad_tareas(self):
        print(f"Hay un total de {self.cantidad_tareas} tareas en el historial de tareas pendientes.")

tareas_pendientes = ListaEnlazada()

while True:
    # Mostrar opciones al usuario
    print("\nOpciones:")
    print("1. Agregar tarea")
    print("2. Eliminar última tarea")
    print("3. Mostrar todas las tareas")
    print("4. Mostrar cantidad total de tareas")
    print("5. Salir")
    
    opcion = int(input("Ingrese el número de opción que desea realizar: "))
    
    if opcion == 1:
        # Agregar tarea al inicio de la lista
        tarea = input("Ingrese la tarea que desea agregar: ")
        tareas_pendientes.agregar_tarea(tarea)
        print(f"Se agregó la tarea '{tarea}' al historial de tareas pendientes.")
    
    elif opcion == 2:
        # Eliminar última tarea de la lista
        tareas_pendientes.eliminar_ultima_tarea()
    
    elif opcion == 3:
        # Mostrar todas las tareas en orden inverso
        tareas_pendientes.mostrar_todas_las_tareas()
    
    elif opcion == 4:
        # Mostrar cantidad total de tareas
        tareas_pendientes.mostrar_cantidad_tareas()
    
    elif opcion == 5:
        break
