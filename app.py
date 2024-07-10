from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Producto
from database import init_app

app = Flask(__name__)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

# Configurar la aplicación Flask 
app.config.from_object('config.Config')

CORS(app)

app = Flask(__name__)

# Configuración CORS para un endpoint específico
cors = CORS(app, resources={r"/agregar_producto": {"origins": "http://127.0.0.1:5500"}})
CORS(app, resources={r"/productos/*": {"origins": "http://127.0.0.1:5500"}})


UPLOAD_FOLDER = 'upload'

# Endpoint para agregar un producto
@app.route('/productos', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    producto = Producto(
        nombre_prod=data['nombre_prod'],
        descripcion=data['descripcion'],
        precio=data['precio'],
        talla=data.get('talla'),
        color=data.get('color'),
        tipo=data['tipo'],
        stock=data['stock'],
        imagen_url=data.get('imagen_url')
    )
    try:
        producto.save()
        return jsonify({'mensaje': 'Producto agregado correctamente', 'producto': producto.serialize()}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    

     

# Ruta principal para mostrar todos los productos en formato JSON
@app.route('/', methods=['GET'])
def mostrar_productos_json():
    # Obtener todos los productos desde la base de datos
    productos = Producto.get_all()
    # Serializar los productos a formato JSON
    productos_json = [producto.serialize() for producto in productos]
    return jsonify(productos_json)


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

#actualiza producto
@app.route('/productos/<int:id_prod>', methods=['PUT'])
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

#elimina producto
@app.route('/productos/<int:id_prod>', methods=['DELETE'])
def delete_producto(id_prod):
    producto = Producto.get_by_id(id_prod)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    producto.delete()
    return jsonify({'message': 'Producto eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)
