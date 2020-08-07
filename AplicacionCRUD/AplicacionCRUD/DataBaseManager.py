import sqlite3

def CreateDataBase():
    myDataBase = sqlite3.connect("Users")
    cursor = myDataBase.cursor()
    cursor.execute('''
            CREATE TABLE UserData(
                id          INTEGER         PRIMARY KEY AUTOINCREMENT,
                user_name   VARCHAR(50),
                password    VARCHAR(50),
                last_name   VARCHAR(20),
                direction   VARCHAR(50),    
                comments    VARCHAR(100)
            )
    ''')
    myDataBase.close()

def InsertTuple(user_name,password,last_name,direction,comments):
    myDataBase = sqlite3.connect("Users")
    cursor = myDataBase.cursor()
    valor=[
        (user_name,password,last_name,direction,comments)
        ]
    cursor.executemany("INSERT INTO UserData VALUES (NULL,?,?,?,?,?)",valor)

    myDataBase.commit()

    myDataBase.close()

def ReadTuple(_id):
    myDataBase = sqlite3.connect("Users")
    cursor = myDataBase.cursor()

    cursor.execute("SELECT * FROM UserData WHERE id=={}".format(_id))
    ret=cursor.fetchall()
    return ret

    myDataBase.close()

def UpdateTuple(_id,_name,_password,_lastName,_direction,_comments):
    myDataBase = sqlite3.connect("Users")
    cursor = myDataBase.cursor()
    sql = '''
        UPDATE UserData
        SET user_name=?, password=?,last_name=?,direction=?,comments=?
        WHERE id==?
    '''

    cursor.execute(sql,(_name,_password,_lastName,_direction,_comments,_id))

    myDataBase.commit()
    myDataBase.close()

def DeleteTuple(_id):
    myDataBase = sqlite3.connect("Users")
    cursor = myDataBase.cursor()

    sql='''
        DELETE FROM UserData
        WHERE id==?
    '''
    cursor.execute(sql,(_id))

    myDataBase.commit()
    myDataBase.close()