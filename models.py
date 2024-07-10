from database import get_db

class Producto:
    def __init__(self, id_prod=None, nombre_prod=None, descripcion=None, precio=None, talla=None, color=None, tipo=None, stock=None, imagen_url=None):
        self.id_prod = id_prod
        self.nombre_prod = nombre_prod
        self.descripcion = descripcion
        self.precio = precio
        self.talla = talla
        self.color = color
        self.tipo = tipo
        self.stock = stock
        self.imagen_url = imagen_url

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_prod:
            cursor.execute("""
                UPDATE productos SET nombre_prod = %s, descripcion = %s, precio = %s, talla = %s, color = %s, tipo = %s, stock = %s, imagen_url = %s
                WHERE id_prod = %s
            """, (self.nombre_prod, self.descripcion, self.precio, self.talla, self.color, self.tipo, self.stock, self.imagen_url, self.id_prod))
        else:
            cursor.execute("""
                INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (self.nombre_prod, self.descripcion, self.precio, self.talla, self.color, self.tipo, self.stock, self.imagen_url))
            self.id_prod = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        productos = []
        for row in rows:
            productos.append(Producto(id_prod=row[0], nombre_prod=row[1], descripcion=row[2], precio=row[3], talla=row[4], color=row[5], tipo=row[6], stock=row[7], imagen_url=row[8]))
        cursor.close()
        return productos

    @staticmethod
    def get_by_id(id_prod):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id_prod = %s", (id_prod,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(id_prod=row[0], nombre_prod=row[1], descripcion=row[2], precio=row[3], talla=row[4], color=row[5], tipo=row[6], stock=row[7], imagen_url=row[8])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_prod = %s", (self.id_prod,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_prod': self.id_prod,
            'nombre_prod': self.nombre_prod,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'talla': self.talla,
            'color': self.color,
            'tipo': self.tipo,
            'stock': self.stock,
            'imagen_url': self.imagen_url
        }
