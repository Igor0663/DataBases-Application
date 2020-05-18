import mysql.connector

def GetRights(login, password):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    args = [login, password, '']
    result_args = cur.callproc('logowanie', args)
    cur.close()
    cnx.close()
    return result_args[2]

def GetUserData(login):
    query = """SELECT * FROM wszyscy_uzytkownicy_dane 
            WHERE login = %s """
    
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    cur.execute(query, (login,))
    user_data = cur.fetchone()
    print(user_data)
    
    cur.close()
    cnx.close()
    return user_data

def ChangeLogin(old, new):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [old, new]
    cur.callproc('zmien_login', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def ChangePwd(login, old, new):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [login, old, new]
    cur.callproc('zmien_haslo', args)
    
    cnx.commit()
    cur.close()
    cnx.close()
