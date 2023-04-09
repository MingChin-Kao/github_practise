from flask_sqlalchemy import SQLAlchemy

# 給定資料庫的必要資訊字典
POSTGRES = {
    'user': 'postgres',
    'password': 'n96111451',
    'db': 'TestDBforCase',
    'host': 'localhost',
    'port': 5432,
}

# 資料庫相關模型定義
db = SQLAlchemy()

class TestTable(db.Model):
    __tablename__ = 'testTable'
    __table_args__ = {"schema": "test_table"}

    idx = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer)
    city = db.Column(db.String)
    HouseholdsOfTypeA = db.Column(db.Integer)
    ElecSalesOfTypeA = db.Column(db.Integer)
    HouseholdsOfTypeB = db.Column(db.Integer)
    ElecSalesOfTypeB = db.Column(db.Integer)
    HouseholdsOfLED = db.Column(db.Integer)
    ElecSalesOfLED = db.Column(db.Integer)