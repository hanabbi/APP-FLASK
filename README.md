# Proyecto Flask - Gestión de Productos

IMPORTANTE: la ruta /productos/ tiene un error de CORS, por lo tanto no funciona los https desde el frontend, excepto el que muestra
a todos los productos. 
En otro momento lo resolveré. 
Cómo debo entregar el proyecto, si bien el resto funciona, asi lo chequeé desde insomnia, 
aún así, paso un script todocuero.sql (Script BBDD todocuero/todocuero.sql) para tener datos iniciales en la bbdd. 

En el frontend, debe ir a Gestión de Productos, allí mostrará el listado de productos y lo resuelve dinámicamente. 
No agregué otros http desde el frontend, ya que el resto al tener ese error de CORS no funcionaría.  
Recuerde que no pudimos exponer, por eso lo explico aquí. 

APP-FRONTEND https://github.com/hanabbi/APP-FRONTEND.git
APP-FLASK https://github.com/hanabbi/APP-FLASK.git


## Descripción

Este proyecto es una API RESTful para gestionar productos utilizando Flask, SQLAlchemy y MySQL. Incluye rutas para crear, leer, actualizar y eliminar productos, así como para listar todos los productos disponibles.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
app-flask-tc/
│
├── app.py                  # Archivo principal que inicia la aplicación Flask y define las rutas.
├── config.py               # Archivo de configuración.
├── database.py             # Archivo para la inicialización de la base de datos y manejo de conexiones.
├── views.py                # Archivo que define las vistas y los controladores para las rutas.
├── models.py               # Archivo que define el modelo `Producto`.
├── requirements.txt        # Dependencias del proyecto.
└── .env                    # Variables de entorno (base de datos, etc.).
```

## Instalación y Configuración

### Requisitos

- Python 3.8+
- MySQL

### Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/hannabi/app-flask-tc.git
cd app-flask-tc
```

2. Crea y activa un entorno virtual:

```bash
python -m venv entorno_virtual_app
source entorno_virtual_app/bin/activate   # En Windows usa: entorno_virtual_app\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno en el archivo `.env`:

```
DB_USERNAME=tu_usuario_de_base_de_datos
DB_PASSWORD=tu_contraseña_de_base_de_datos
DB_HOST=localhost
DB_NAME=nombre_de_tu_base_de_datos
DB_PORT=3306
```

### Ejecución

Ejecuta la aplicación:

```
bash python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## Rutas de la API

- `GET /` - Ruta de prueba.
- `POST /productos/` - Crear un nuevo producto.
- `GET /productos/` - Obtener todos los productos.
- `GET /productos/<int:id_prod>` - Obtener un producto por su ID.
- `PUT /productos/<int:id_prod>` - Actualizar un producto por su ID.
- `DELETE /productos/<int:id_prod>` - Eliminar un producto por su ID.

## Ejemplo de Solicitud

### Crear un Producto

```bash
curl -X POST http://127.0.0.1:5000/api/productos/ \
     -H "Content-Type: application/json" \
     -d '{
           "nombre_prod": "Producto 1",
           "descripcion": "Descripción del producto 1",
           "precio": 100,
           "talla": "M",
           "color": "Rojo",
           "tipo": "Ropa",
           "stock": 10,
           "imagen_url": "http://imagen.com/producto1.jpg"
         }'
```

