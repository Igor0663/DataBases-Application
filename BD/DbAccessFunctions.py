import mysql.connector

def Login(login, password):
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
    #print(user_data)
    
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

def ChangeName(who, whom, new):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, whom, new]
    cur.callproc('zmien_imie', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def ChangeSname(who, whom, new):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, whom, new]
    cur.callproc('zmien_nazwisko', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def ChangeDep(who, whom, new):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, whom, new]
    cur.callproc('zmien_dzial', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def GetDepartments():
    query = """SELECT nazwa_dzialu FROM dzial """
    
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    cur.execute(query)
    dep_data = cur.fetchall()
    departments = []
    for dep in dep_data:
        departments.append(dep[0])
    
    cur.close()
    cnx.close()
    return departments

def GetRights():
    query = """SELECT nazwa_uprawnienia FROM uprawnienia """
    
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    cur.execute(query)
    rig_data = cur.fetchall()
    rights = []
    for rig in rig_data:
        rights.append(rig[0])
    
    cur.close()
    cnx.close()
    return rights

def ChangeRig(who, whom, new):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, whom, new]
    cur.callproc('zmien_uprawnienia', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def GetUsers():
    query = """SELECT login FROM uzytkownik """
    
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    cur.execute(query)
    usr_data = cur.fetchall()
    users = []
    for usr in usr_data:
        users.append(usr[0])
    
    cur.close()
    cnx.close()
    return users