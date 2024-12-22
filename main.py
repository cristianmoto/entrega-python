from base_datos import crear_base_datos
from inventario import Inventario
from colorama import init, Fore, Style

init(autoreset=True)

def menu():
    crear_base_datos()  
    inventario = Inventario()
    while True:
        print(Fore.GREEN + "\n--- Menú de Inventario ---")
        print(Fore.YELLOW + "1. Registrar Producto")
        print(Fore.YELLOW + "2. Actualizar Producto")
        print(Fore.YELLOW + "3. Eliminar Producto")
        print(Fore.YELLOW + "4. Mostrar Productos")
        print(Fore.YELLOW + "5. Buscar Producto")
        print(Fore.YELLOW + "6. Generar Reporte de Productos con Bajo Stock")
        print(Fore.RED + "7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            categoria = input("Categoría del producto: ")
            inventario.registrar_producto(nombre, descripcion, cantidad, precio, categoria)
        elif opcion == "2":
            id = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre del producto (dejar en blanco para mantener): ")
            descripcion = input("Nueva descripción del producto (dejar en blanco para mantener): ")
            cantidad = input("Nueva cantidad del producto (dejar en blanco para mantener): ")
            precio = input("Nuevo precio del producto (dejar en blanco para mantener): ")
            categoria = input("Nueva categoría del producto (dejar en blanco para mantener): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, nombre or None, descripcion or None, cantidad, precio, categoria or None)
        elif opcion == "3":
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == "4":
            inventario.mostrar_productos()
        elif opcion == "5":
            id = int(input("ID del producto a buscar: "))
            inventario.buscar_producto(id)
        elif opcion == "6":
            bajo_stock = int(input("Ingrese el nivel de stock bajo: "))
            inventario.generar_reporte_stock(bajo_stock)
        elif opcion == "7":
            print(Fore.RED + "Saliendo del sistema...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
