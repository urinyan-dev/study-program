from flask import Flask

app = Flask(__name__)
print(app)


@app.route('/')
def home():
    return 'hello flask'


app.run()

print('aaaあaaaaaaaadadwadwadadああああaaああa')
