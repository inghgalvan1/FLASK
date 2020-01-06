from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return  "hola Codi"

@app.route('/usuario/<username>')
def usuario(username):

    return  "hola " + username

if __name__ == '__main__':
    app.run(debug=True,port = 9000) 