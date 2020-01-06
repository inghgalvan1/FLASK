from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Hector Galvan"
    course = "Python web"
    is_premium = False
    Courses = ["Rubi","Python","C++","javascript"]
    
    return  render_template('index.html',username=name, coursename=course, is_premium=is_premium,Courses=Courses)

if __name__ == '__main__':
    app.run(debug=True,port = 9000) 