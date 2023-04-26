# main.py
 
from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route('/mingchin')
def mingchin():
    return render_template('mingchin.html')

@app.route('/show_csv')
def show_csv():
    data = pd.read_csv('./static/data.csv', encoding='big5')
    data_dict = data.to_dict(orient='records')
    data_header = list(data_dict[0].keys())
    print("data dict is ", data_dict)
    return render_template('show_csv.html', data_header=data_header, datas=data_dict)


@app.route('/HongEn')
def index():
    return render_template('index.html')


@app.route('/ChiaHong')
def ChiaHong():
    return render_template('ChiaHong.html')

