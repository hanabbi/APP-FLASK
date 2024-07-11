CREATE DATABASE todocuero;

USE todocuero;

CREATE TABLE usuarios (
  id_usuario INT NOT NULL AUTO_INCREMENT,  -- Primary Key with Auto Increment
  nombre_usuario VARCHAR(255) NOT NULL UNIQUE,
  passwd_usuario VARCHAR(255) NOT NULL,  -- Consider using a hashing algorithm for password storage
  nivel ENUM('admin', 'cliente') NOT NULL DEFAULT 'cliente',  -- Predefined user levels
  email VARCHAR(255) NOT NULL,  -- Unique email for each user
  PRIMARY KEY (id_usuario)  -- Define id_usuario as the primary key
);

CREATE TABLE productos (
  id_prod INT NOT NULL AUTO_INCREMENT,  -- Primary Key with Auto Increment
  nombre_prod VARCHAR(255) NOT NULL,
  descripcion TEXT,  -- Allows for longer product descriptions
  precio DECIMAL(10,2) NOT NULL,  -- Stores prices with two decimal places
  talla VARCHAR(50),
  color VARCHAR(50),
  tipo ENUM('indumentaria', 'calzado', 'carteras', 'accesorios'),
  stock INT NOT NULL DEFAULT 0,  -- Default stock of 0
  imagen_url VARCHAR(255),
  PRIMARY KEY (id_prod)  -- Define id_prod as the primary key
);

INSERT INTO usuarios (nombre_usuario, passwd_usuario, nivel, email)
VALUES
  ('admin', 'admin', 'admin', 'admin@todocuero.com'),
  ('cliente', 'cliente', 'cliente', 'cliente@todocuero.com');


-- Indumentaria de cuero
INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Campera de Cuero hombre', 'Campera de cuero con diseño clásico.', 299.99, 'M', 'Negro', 'indumentaria', 10, 'upload/producto1');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Pantalones de Cuero Elegantes', 'Pantalones de cuero elegantes para ocasiones especiales.', 149.99, 'L', 'Marrón', 'indumentaria', 15, 'upload/producto2');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Bolso de Cuero Clásico', 'Bolso de cuero clásico para uso diario.', 199.99, NULL, 'Negro', 'indumentaria', 8, 'upload/producto3');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Chaqueta de Cuero Slim Fit', 'Chaqueta de cuero slim fit para hombres.', 259.99, 'XL', 'Negro', 'indumentaria', 12, 'upload/producto4');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Falda de Cuero Elegante', 'Falda de cuero elegante para mujeres.', 129.99, 'S', 'Negro', 'indumentaria', 10,'upload/producto5');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Cinturón de Cuero Clásico', 'Cinturón de cuero clásico con hebilla elegante.', 49.99, NULL, 'Marrón', 'indumentaria', 20, 'upload/producto6');

-- Calzado
INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Botas de Cuero Alto', 'Botas de cuero alto para hombres.', 199.99, '42', 'Negro', 'calzado', 10, 'upload/producto7');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Zapatos de Cuero Elegantes', 'Zapatos de cuero elegantes para ocasiones formales.', 159.99, '40', 'Marrón', 'calzado', 15, 'upload/producto8');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Sneakers de Cuero Modernos', 'Sneakers de cuero modernos para un estilo casual.', 129.99, '38', 'Blanco', 'calzado', 20, 'upload/producto9');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Sandalias de Cuero Verano', 'Sandalias de cuero para el verano.', 89.99, '39', 'Negro', 'calzado', 18, 'upload/producto10');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Mocasines de Cuero Casual', 'Mocasines de cuero para un look casual.', 109.99, '41', 'Marrón', 'calzado', 15, 'upload/producto11');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Botines de Cuero Urbano', 'Botines de cuero para un estilo urbano.', 179.99, '43', 'Negro', 'calzado', 12, 'upload/producto12');

-- Carteras
INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Cartera de Cuero Compacta', 'Cartera de cuero compacta para tarjetas y billetes.', 79.99, NULL, 'Negro', 'carteras', 15, 'upload/producto13');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Bolso de Cuero Elegante', 'Bolso de cuero elegante para llevar documentos y dispositivos.', 149.99, NULL, 'Marrón', 'carteras', 10, 'upload/producto14');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Cartera de Mano Cuero Clásica', 'Cartera de mano de cuero clásica para ocasiones formales.', 99.99, NULL, 'Negro', 'carteras', 12, 'upload/producto15');

-- Accesorios
INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Cinturón de Cuero Casual', 'Cinturón de cuero casual para uso diario.', 59.99, NULL, 'Marrón', 'accesorios', 18, 'upload/producto16');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Pulsera de Cuero Moderna', 'Pulsera de cuero moderna para hombres.', 39.99, NULL, 'Negro', 'accesorios', 20, 'upload/producto17');

INSERT INTO productos (nombre_prod, descripcion, precio, talla, color, tipo, stock, imagen_url)
VALUES ('Estuche de Cuero para Gafas', 'Estuche de cuero elegante para gafas de sol.', 29.99, NULL, 'Marrón', 'accesorios', 15, 'producto18');

select * from productos;
select * from usuarios;
