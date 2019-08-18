from form import EmailForm
from form import LoginForm
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm(request.form)
    flag = False
    name = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        email = form.email.data
        name = form.name.data
        if email != '' and name != '':
            print(f"Nombre capturado: {name}")
            print(f"Email capturado: {email}")
            flag = True

    return render_template('index.html', flag=flag, name=name)


@app.route('/admin', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    login_error = False

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.username.data == 'admin' and form.password.data == 'admin':
            return render_template('tables.html')
        else:
            login_error = True
    return render_template('login.html', login_error=login_error)


@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
