POSTGRES = {
    'user': 'postgres',
    'password': 'n96111451',
    'database': 'TestDBforCase',
    'host': 'localhost',
    'port': 5432,
    'schema': 'test_table',
    'table' : 'testTable',
    'tableColumn' :{
        1:{
            'name' : 'idx',
            'dataType' : 'integer',
            'canNull' : False,
            'isPK' : True
        },
        2:{
            'name' : 'year',
            'dataType' : 'integer',
            'canNull' : True,
            'isPK' : False
        },
        3:{
            'name' : 'city',
            'dataType' : 'text',
            'canNull' : True,
            'isPK' : False
        },
        4:{
            'name' : 'HouseholdsOfTypeA',
            'dataType' : 'integer',
            'canNull' : True,
            'isPK' : False
        },
        5:{
            'name' : 'ElecSalesOfTypeA',
            'dataType' : 'integer',
            'canNull' : True,
            'isPK' : False
        },
        6:{
            'name' : 'HouseholdsOfTypeB',
            'dataType' : 'integer',
            'canNull' : True,
            'isPK' : False
        },
        7:{
            'name' : 'ElecSalesOfTypeB',
            'dataType' : 'integer',
            'canNull' : True,
            'isPK' : False
        },
        8:{
            'name' : 'HouseholdsOfLED',
            'dataType' : 'integer',
            'canNull' : True,
            'isPK' : False
        },
        9:{
            'name' : 'ElecSalesOfLED',
            'dataType' : 'integer',
            'canNull' : True,
            'isPK' : False
        }
    }
}