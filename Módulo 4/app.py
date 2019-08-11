from form import AgeForm
from form import legal_or_not
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form_url():
    form = AgeForm(request.form)

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        return render_template('success.html',
                               name=form.name.data,
                               legal=legal_or_not(form.age.data))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
