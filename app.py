from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Producto
from database import init_app
#from views import *

app = Flask(__name__)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

# Configurar la aplicación Flask 
app.config.from_object('config.Config')

CORS(app)


# Ruta principal para mostrar todos los productos en formato JSON
@app.route('/', methods=['GET'])
def mostrar_productos_json():
    # Obtener todos los productos desde la base de datos
    productos = Producto.get_all()
    # Serializar los productos a formato JSON
    productos_json = [producto.serialize() for producto in productos]
    return jsonify(productos_json)


@app.route('/productos', methods=['POST'])
def create_producto():
        data = request.json
        nuevo_producto = Producto(nombre_prod=data['nombre_prod'], descripcion=data['descripcion'], precio=data['precio'], talla=data['talla'], color=data['color'], tipo=data['tipo'], stock=data['stock'], imagen_url=data['imagen_url'])
        nuevo_producto.save()
        return jsonify({'mensaje': 'Producto agregado correctamente'}), 201
   
    
#trae todos los productos
@app.route('/productos/', methods=['GET'])
def get_all_productos():
    productos = Producto.get_all()
    return jsonify([producto.serialize() for producto in productos])

#trae un producto específico
@app.route('/productos/<int:id_prod>', methods=['GET'])
def get_producto(id_prod):
    producto = Producto.get_by_id(id_prod)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    return jsonify(producto.serialize())

@app.route('/productos/<int:id_prod>', methods=['PUT'])
def update_producto(id_prod):
    producto = Producto.get_by_id(id_prod)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    
    data = request.json
    producto.nombre_prod = data.get('nombre_prod', producto.nombre_prod)
    producto.descripcion = data.get('descripcion', producto.descripcion)
    producto.precio = data.get('precio', producto.precio)
    producto.talla = data.get('talla', producto.talla)
    producto.color = data.get('color', producto.color)
    producto.tipo = data.get('tipo', producto.tipo)
    producto.stock = data.get('stock', producto.stock)
    producto.imagen_url = data.get('imagen_url', producto.imagen_url)
    producto.save()
    
    return jsonify({'message': 'Producto actualizado exitosamente'})

#elimina producto
@app.route('/productos/<int:id_prod>', methods=['DELETE'])
def delete_producto(id_prod):
    producto = Producto.get_by_id(id_prod)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    producto.delete()
    return jsonify({'message': 'Producto eliminado exitosamente'})

"""
# Rutas para el CRUD de Producto
app.route('/', methods=['GET'])(mostrar_productos_json)
app.route('/productos/', methods=['POST'])(create_producto)
app.route('/productos/', methods=['GET'])(get_all_productos)
app.route('/productos/<int:movie_id>', methods=['GET'])(get_producto)
app.route('/productos/<int:movie_id>', methods=['PUT'])(update_producto)
app.route('/productos/<int:movie_id>', methods=['DELETE'])(delete_producto)
"""

if __name__ == '__main__':
    app.run(debug=True)
