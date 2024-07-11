from flask import jsonify, request
from models import Producto

def index():
    return jsonify({'message': 'Hello World API Productos'})

def mostrar_productos_json():
    # Obtener todos los productos desde la base de datos
    productos = Producto.get_all()
    # Serializar los productos a formato JSON
    productos_json = [producto.serialize() for producto in productos]
    return jsonify(productos_json)

def create_producto():
    data = request.json
    nuevo_producto = Producto(
        nombre_prod=data['nombre_prod'],
        descripcion=data['descripcion'],
        precio=data['precio'],
        talla=data['talla'],
        color=data['color'],
        tipo=data['tipo'],
        stock=data['stock'],
        imagen_url=data['imagen_url']
    )
    nuevo_producto.save()
    return jsonify({'message': 'Producto creado exitosamente'}), 201

def get_all_productos():
    productos = Producto.get_all()
    return jsonify([producto.serialize() for producto in productos])

def get_producto(id_prod):
    producto = Producto.get_by_id(id_prod)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    return jsonify(producto.serialize())


def update_producto(id_prod):
    producto = Producto.get_by_id(id_prod)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    data = request.json
    producto.nombre_prod = data['nombre_prod']
    producto.descripcion = data['descripcion']
    producto.precio = data['precio']
    producto.talla = data['talla']
    producto.color = data['color']
    producto.tipo = data['tipo']
    producto.stock = data['stock']
    producto.imagen_url = data['imagen_url']
    producto.save()
    return jsonify({'message': 'Producto actualizado exitosamente'})


def delete_producto(id_prod):
    producto = Producto.get_by_id(id_prod)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    producto.delete()
    return jsonify({'message': 'Producto eliminado exitosamente'})
