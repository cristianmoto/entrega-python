from base_datos import registrar_producto, actualizar_producto, eliminar_producto, mostrar_productos, buscar_producto_por_id, generar_reporte_stock

class Inventario:
    def __init__(self):
        pass

    def registrar_producto(self, nombre, descripcion, cantidad, precio, categoria):
        registrar_producto(nombre, descripcion, cantidad, precio, categoria)

    def actualizar_producto(self, id, nombre=None, descripcion=None, cantidad=None, precio=None, categoria=None):
        actualizar_producto(id, nombre, descripcion, cantidad, precio, categoria)

    def eliminar_producto(self, id):
        eliminar_producto(id)

    def mostrar_productos(self):
        productos = mostrar_productos()
        for producto in productos:
            print(producto)

    def buscar_producto(self, id):
        producto = buscar_producto_por_id(id)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    def generar_reporte_stock(self, bajo_stock):
        productos = generar_reporte_stock(bajo_stock)
        print("Productos con bajo stock:")
        for producto in productos:
            print(producto)
