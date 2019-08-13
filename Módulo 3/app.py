from flask import Flask
from flask import request
from flask import render_template

# Creamos una instancia de Flask:
app = Flask(__name__)


# Defino la ruta principal:
@app.route('/')
def index():
    return render_template("index.html")


# Defino la ruta acerca de:
@app.route('/acerca-de')
def about():
    return render_template("acerca-de.html")


# Ruta saludos:
@app.route('/saludos')
def hola():
    name = "Rodolfo"
    return render_template("saludo.html", nombre=name)


# Ruta saludos personalizados:
@app.route('/saludos/<string:name>')
def hola_nombre(name):
    return render_template("saludo.html", nombre=name)


# Ruta de productos:
@app.route('/producto/<int:id>/<string:name>/<int:stock>')
def mostrar_producto(id, name, stock):
    return render_template("producto.html",
                           id=id, nombre=name, bodega=stock)


# Ruta para catálogo:
@app.route('/productos')
def productos():
    productos = {
        'item1': {
            'id': 1234,
            'name': "Babero de dinosario",
            'cost': 35.15,
            'stock': True,
            'photo': "https://cdn.shopify.com/s/files/1/0019/4088/1454/products/micumacubaberoplastificadodino_1024x1024.jpg"
        },
        'item2': {
            'id': 4321,
            'name': "Zapatos de bebé",
            'cost': 150.78,
            'stock': False,
            'photo': "https://cdn.shopify.com/s/files/1/1628/6583/products/SH045.3_1024x1024.jpg"
        }
    }
    return render_template("productos.html", productos=productos)


# Error 404:
@app.errorhandler(404)
def no_encontrado(error=None):
    return f"<h1>ERROR – Ruta no encontrada: {request.url}</h1>"


if __name__ == '__main__':
    # Mi servidor escucha peticiones:
    app.run(debug=True)
