from form import AgeForm
from form import EmailForm
from form import legal_or_not
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm(request.form)
    flag = False

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.email.data is not None:
            print(f"Email capturado: {form.email.data}")
            flag = True

    return render_template('index.html', flag=flag)


@app.route('/form', methods=['GET', 'POST'])
def form_url():
    form = AgeForm(request.form)
    no_data = False

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.name.data is not None and form.age.data is not None:
            return render_template('success.html',
                                   name=form.name.data,
                                   legal=legal_or_not(form.age.data))
        else:
            no_data = True
    return render_template('form.html', flag=no_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
