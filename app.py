import flask
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('main.html', title="Home", content="Hello, World!") 
@app.route('/pk/<id>', methods=['GET'])
def pk(id):
    return id

app.run()