Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Ropa:
    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

class TiendaRopa:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, codigo, descripcion, precio, stock):
        producto = Ropa(codigo, descripcion, precio, stock)
        self.inventario.append(producto)
        print(f"Producto '{descripcion}' agregado al inventario.")

    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.inventario:
                print(f"Código: {producto.codigo}, Descripción: {producto.descripcion}, Precio: ${producto.precio}, Stock: {producto.stock}")

    def vender_producto(self, codigo, cantidad):
        for producto in self.inventario:
            if producto.codigo == codigo:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f"Venta exitosa. Total a pagar: ${producto.precio * cantidad}")
                else:
                    print("Stock insuficiente para realizar la venta.")
                return
        print("Producto no encontrado en el inventario.")

# Ejemplo de uso
tienda = TiendaRopa()

tienda.agregar_producto(1, "Camisa", 20.0, 50)
tienda.agregar_producto(2, "Pantalón", 30.0, 30)
tienda.agregar_producto(3, "Sudadera", 40.0, 20)

tienda.mostrar_inventario()

tienda.vender_producto(1, 10)

tienda.mostrar_inventario()
