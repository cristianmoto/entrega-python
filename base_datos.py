import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )7
    ''')
    conexion.commit()
    conexion.close()

def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    conexion.close()

def actualizar_producto(id, nombre=None, descripcion=None, cantidad=None, precio=None, categoria=None):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    query = 'UPDATE productos SET '
    params = []
    if nombre:
        query += 'nombre = ?, '
        params.append(nombre)
    if descripcion:
        query += 'descripcion = ?, '
        params.append(descripcion)
    if cantidad is not None:
        query += 'cantidad = ?, '
        params.append(cantidad)
    if precio is not None:
        query += 'precio = ?, '
        params.append(precio)
    if categoria:
        query += 'categoria = ? '
        params.append(categoria)
    query += 'WHERE id = ?'
    params.append(id)
    cursor.execute(query, tuple(params))
    conexion.commit()
    conexion.close()

def eliminar_producto(id):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM productos WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()

def mostrar_productos():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conexion.close()
    return productos

def buscar_producto_por_id(id):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos WHERE id = ?', (id,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def generar_reporte_stock(bajo_stock):
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos WHERE cantidad <= ?', (bajo_stock,))
    productos = cursor.fetchall()
    conexion.close()
    return productos
