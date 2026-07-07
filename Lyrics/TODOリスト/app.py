from flask import Flask, render_template, request, redirect, jsonify  # noqa

app = Flask(__name__)

todos = []
# api_todos = {}
# todos_index = 0


@app.route('/')
def home():
    return render_template('home.html', todos=todos)


# @app.route('/api/todos', methods=['GET'])
# def get_todos():
    # return jsonify(todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append(todo)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    index = int(request.form['index'])
    todos.pop(index)
    return redirect('/')


@app.route('/tool/add', methods=['POST'])
def api_add():
    todo = request.form['todo']
    todos.append(todo)
    print(jsonify(todos))
    return jsonify(todos)


app.run(debug=True)
