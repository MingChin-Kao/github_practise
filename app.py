# main.py
 
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/mingchin')
def mingchin():
    return render_template('mingchin.html')

print("hello")
@app.route('/HongEn')
def HongEn():
    return render_template('HongEn.html')

print("hello")
