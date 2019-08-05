import yaml
from flask import Flask
from flask import request
from flask import render_template

# Create a Flask app instance
app = Flask(__name__)


@app.route('/')
def index():
    """Base route."""

    return render_template('index.html')


@app.route('/material')
def material():
    """Route for material section."""

    with open('material.json', 'r') as file:
        data = file.read()

    material = yaml.load(data)
    return render_template('material.html', material=material)


@app.errorhandler(404)
def not_found(error=None):
    """Error handling route (404)."""

    return render_template('404.html', url=request.url)


if __name__ == '__main__':
    # app.run(debug=True, port=8000)
    app.run()
