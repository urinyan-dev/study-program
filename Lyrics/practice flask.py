from flask import Flask, render_template, request  # noqa

app = Flask(__name__)
items = ['a', 'b', 'c']


@app.route('/')
def home():
    return render_template('home.html', items=items)
    # return 'hello flask'


@app.route('/user/<name>')
def user(name):
    return f'こんにちは{name}さん'


@app.route('/form')
def form():
    return render_template('form.html')


app.run(debug=True)
