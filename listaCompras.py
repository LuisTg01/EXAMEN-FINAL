class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def imprimir(self):
        
        print("Lista de compras")
        print(self.items)
            
def agregarCompra():
    agregar = input("Añadir producto: ")
    c.agregar(agregar)
    print('Se añadió el producto')

def eliminarCompra():
    print("Se quito:")
    print(c.avanzar())
    

#Programa Principal

c = Cola()
while True:
    print("Menú")
    print("[1]Agregar producto")
    print("[2]Eliminar producto")
    print("[3]Mostrar productos")
    print("[0]salir")
    n = int(input("Ingrese opción: "))
    if n == 1:
        agregarCompra()
    elif n == 2:
        eliminarCompra()
    elif n ==3:
        c.imprimir()
    elif n == 0:
        break