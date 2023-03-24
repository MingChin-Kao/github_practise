from flask import Flask, render_template
app = Flask(__name__)

print("hello")
@app.route('/HongEn')
def index():
    return render_template('index.html')
set FLASK_APP=app.py

print("hello")