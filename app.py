# main.py
import pandas as pd
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/mingchin')
def mingchin():
    return render_template('mingchin.html')


df = pd.read_csv('data.csv')
df.to_csv('data.csv', index=None)
@app.route('/HongEn')
def index():
    data = pd.read_csv('data.csv')
    return render_template('index.html', pie_chart=data)




@app.route('/ChiaHong')
def ChiaHong():
    return render_template('ChiaHong.html')

print("hello")
