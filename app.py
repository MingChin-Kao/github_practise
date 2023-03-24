# main.py
 
from flask import Flask, render_template
app = Flask(__name__)

print("hello")

@app.route('/mingchin')
def mingchin():
    return render_template('mingchin.html')


@app.route('/HongEn')
def index():
    return render_template('index.html')


print("hello")

@app.route('/ChiaHong')
def ChiaHong():
    return render_template('ChiaHong.html')

print("hello")
