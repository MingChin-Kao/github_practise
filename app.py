# main.py
import pandas as pd
import numpy as np
import csv
from flask import Flask, render_template
app = Flask(__name__)

print("hello")

@app.route('/mingchin')
def mingchin():
    return render_template('mingchin.html')


@app.route('/HongEn')
def index():
    data = pd.read_csv("C:\\Users\\Brian\\Downloads\\data.csv",encoding= 'big5')
    # data.columns = range(data.shape[1])
    # print(data)
    chart=[]
    column_names=[]
    for i in data.T:
        chart.append(data.T[i][6])
    chart_int=[int(i) for i in chart]
    column_names=list(data.columns)
    col_name=[str(i) for i in column_names]
    return render_template('index.html',rows =data.T,data_chart=chart_int, col = column_names, chart_label=col_name, titles=[''])




print("hello")

@app.route('/ChiaHong')
def ChiaHong():
    return render_template('ChiaHong.html')

print("hello")
