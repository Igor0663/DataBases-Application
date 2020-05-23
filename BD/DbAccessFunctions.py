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
    query = """SELECT login FROM uzytkownik"""
    
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

def GetUsersNamesLogins():
    query = """SELECT * FROM wszyscy_uzytkownicy_dane ORDER BY nazwisko """
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    

    cur.execute(query)
    usr_data = cur.fetchall()
    users = []
    for usr in usr_data:
        users.append([f"{usr[0]} {usr[1]} ({usr[3]})", usr[2]])

    cur.close()
    cnx.close()
    return users

def AddNewUser(who, newname, newsname, newlogin, newpwd, department, rights):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, newname, newsname, newlogin, newpwd, department, rights]
    cur.callproc('dodaj_uzytkownika', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def DeleteUser(who, user):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, user]
    cur.callproc('usun_uzytkownika_login', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def UserBasicData(login):
    query = """SELECT * FROM wszyscy_uzytkownicy_dane WHERE login = %s """
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    cur.execute(query, (login,))
    usr = cur.fetchone()
    user = f"{usr[0]} {usr[1]} ({usr[3]})"

    cur.close()
    cnx.close()
    return user

def Equipment():
    query = """SELECT * FROM sprzet """
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)

    cur.execute(query)
    eqp = cur.fetchall()

    cur.close()
    cnx.close()
    return eqp

def UsableEquipmentKind():
    query = """SELECT rodzaj FROM rodzaj_sprzetu_z """
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)

    cur.execute(query)
    eqp = cur.fetchall()
    equip = []
    for x in eqp:
        equip.append(x[0])

    cur.close()
    cnx.close()
    return equip

def AddEqpUs(who, eqpname, amount, kind):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, eqpname, amount, kind]
    cur.callproc('dodaj_sprzet_z', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def UnUsableEquipmentKind():
    query = """SELECT rodzaj FROM rodzaj_sprzetu_nz """
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)

    cur.execute(query)
    eqp = cur.fetchall()
    equip = []
    for x in eqp:
        equip.append(x[0])

    cur.close()
    cnx.close()
    return equip

def AddEqpUnUs(who, eqpname, kind):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, eqpname, kind]
    cur.callproc('dodaj_sprzet_nz', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def AddEqpUsKind(who, kindname):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, kindname]
    cur.callproc('dodaj_rodzaj_sprzetu_z', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def AddEqpUnUsKind(who, kindname, maxdays):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, kindname, maxdays]
    cur.callproc('dodaj_rodzaj_sprzetu_nz', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def GetDebtUsers():
    query = """SELECT * FROM uzytkownicy_zadluzeni """
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    

    cur.execute(query)
    usr_data = cur.fetchall()
    users = []
    for usr in usr_data:
        users.append(f"{usr[0]} {usr[1]} ({usr[2]}) : usr[3] : usr[4]")

    cur.close()
    cnx.close()
    return users

def DeleteUsKind(who, kindname):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, kindname]
    cur.callproc('usun_rodzaj_sprzetu_z', args)
    
    cnx.commit()
    cur.close()
    cnx.close()

def DeleteUnUsKind(who, kindname):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    
    args = [who, kindname]
    cur.callproc('usun_rodzaj_sprzetu_nz', args)
    
    cnx.commit()
    cur.close()
    cnx.close()