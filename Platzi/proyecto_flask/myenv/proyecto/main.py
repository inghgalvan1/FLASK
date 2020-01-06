from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Hector Galvan"
    course = "Python web"
    
    return  render_template('index.html',username=name, coursename=course)

if __name__ == '__main__':
    app.run(debug=True,port = 5000) 