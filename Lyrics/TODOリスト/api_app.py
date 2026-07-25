from flask import Flask, render_template, request, redirect, jsonify  # noqa

app = Flask(__name__)

todos = []
# api_todos = {}
# todos_index = 0


@app.route('/')
def home():
    return render_template('api_home.html', todos=todos)


@app.route('/tool/add', methods=['POST'])
def api_add():
    todo = request.json['todo']
    todos.append(todo)
    return jsonify(todos)


@app.route('/delete', methods=['POST'])
def delete():
    index = int(request.form['index'])
    todos.pop(index)
    return redirect('/')


app.run(debug=True)
