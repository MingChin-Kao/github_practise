# main.py
from flask import Flask, render_template
from CH_DBModel import db, TestTable # 引入資料庫相關的東西，已經打包成一個 py 檔案
from CH_DBRequiredInformation import POSTGRES
from CH_queryDB import queryDB
from CH_insertDB import write_random_data

app = Flask(__name__)

print("hello")

@app.route('/mingchin')
def mingchin():
    return render_template('mingchin.html')


@app.route('/HongEn')
def index():
    return render_template('index.html')

@app.route('/ChiaHong')
def ChiaHong():
    return render_template('ChiaHong.html')

# 設定資料庫相關的連線內容
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(password)s@%(host)s:%(port)s/%(database)s' % POSTGRES

# 初始化資料庫模型
db.init_app(app)

# 資料庫查詢並顯示的路由
@app.route('/query_db')
def query_db():
    # 查詢 TestTable 資料表中的所有資料
    rows = queryDB(TestTable)
    return render_template('queryPage.html', rows=rows)

@app.route('/db_insert')
def db_insert():
    # 資料表為空的話取 idx 會報錯，因此直接給 0
    try:
        lastIdx = queryDB(TestTable)[-1].idx
    except:
        lastIdx = 0

    # 防呆，其實可以不用
    if lastIdx is not None:
        write_random_data('static/data.csv', db, lastIdx)

    return 'ok'

print("hello")
