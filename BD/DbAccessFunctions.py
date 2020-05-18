import mysql.connector

def GetRights(login, password):
    cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
    cur = cnx.cursor(buffered=True)
    args = [login, password, '']
    result_args = cur.callproc('logowanie', args)
    cnx.close()
    return result_args[2]

def GetUserData(login):
    return [login]