from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from DbAccessFunctions import GetUserData
from DbAccessFunctions import ChangeLogin
from DbAccessFunctions import ChangePwd
from DbAccessFunctions import GetRights
from DbAccessFunctions import ChangeName

class AccountSettingsScreen(Screen):
    logcont = ObjectProperty(None)
    pwdcont = ObjectProperty(None)
    namecont = ObjectProperty(None)
    snamecont = ObjectProperty(None)
    depcont = ObjectProperty(None)
    rigcont = ObjectProperty(None)

    logbtn = ObjectProperty(None)
    pwdbtn = ObjectProperty(None)
    namebtn = ObjectProperty(None)
    snamebtn = ObjectProperty(None)
    depbtn = ObjectProperty(None)
    rigbtn = ObjectProperty(None)

    bckbtn = ObjectProperty(None)


    def UpdateData(self):        
        app = App.get_running_app()
        user_data = GetUserData(app.root.login)
        self.logcont.text = user_data[2]
        self.namecont.text = user_data[1]
        self.snamecont.text = user_data[0]
        self.depcont.text = user_data[3]
        self.rigcont.text = app.root.rig
        if app.root.rig == "czlonek_kola":
            self.logbtn.disabled = True
            self.namebtn.disabled = True
            self.snamebtn.disabled = True
            self.depbtn.disabled = True
            self.rigbtn.disabled = True

    def GetBack(self):
        app = App.get_running_app()
        if app.root.rig == "czlonek_kola":
            Window.size = (400, 160)
            app.root.current = "opcje czlonka kola"
        elif app.root.rig == "administrator":
            Window.size = (400, 360)
            app.root.current = "opcje administratora"
    
    def ChangeLogin(self):
        app = App.get_running_app()
        Window.size = (400, 160)
        app.root.current = "zmiana loginu"

    def ChangePwd(self):
        app = App.get_running_app()
        Window.size = (400, 200)
        app.root.current = "zmiana hasla"

    def ChangeName(self):
        app = App.get_running_app()
        Window.size = (400, 160)
        app.root.current = "zmiana imienia"

class ChangeLoginScreen(Screen):
    newlog = ObjectProperty(None)
    newlog2 = ObjectProperty(None)
    accbtn = ObjectProperty(None)
    bckbtn = ObjectProperty(None)

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def SubmitNewLogin(self):
        if(self.newlog.text == self.newlog2.text and len(self.newlog.text) >= 6):
            app = App.get_running_app()
            ChangeLogin(app.root.login, self.newlog.text)
            app.root.login = self.newlog.text
            screen = app.root.get_screen("ustawienia konta")
            screen.UpdateData()
            Window.size = (400, 360)
            app.root.current = "ustawienia konta"
            self.ClearInput()
            
    def ClearInput(self):
        self.newlog.text = ""
        self.newlog2.text = ""


class ChangePwdScreen(Screen):
    oldpwd = ObjectProperty(None)
    newpwd = ObjectProperty(None)
    newpwd2 = ObjectProperty(None)
    accbtn = ObjectProperty(None)
    bckbtn = ObjectProperty(None)

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def SubmitNewPwd(self):
        app = App.get_running_app()
        if(GetRights(app.root.login, self.oldpwd.text) and  self.newpwd.text == self.newpwd2.text and len(self.newpwd.text) >= 6):
            ChangePwd(app.root.login, self.oldpwd.text, self.newpwd.text)
            Window.size = (400, 360)
            app.root.current = "ustawienia konta"
        self.ClearInput()

    def ClearInput(self):
        self.oldpwd.text = ""
        self.newpwd.text = ""
        self.newpwd2.text = ""  

class ChangeNameScreen(Screen):
    newname = ObjectProperty(None)
    newname2 = ObjectProperty(None)
    accbtn = ObjectProperty(None)
    bckbtn = ObjectProperty(None)

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()
    def SubmitNewName(self):
        if(self.newname.text == self.newname2.text and len(self.newname.text) >= 3):
            app = App.get_running_app()
            ChangeName(app.root.login, app.root.login, self.newname.text)
            screen = app.root.get_screen("ustawienia konta")
            screen.UpdateData()
            Window.size = (400, 360)
            app.root.current = "ustawienia konta"
            self.ClearInput()

    def ClearInput(self):
        self.newname.text = ""
        self.newname2.text = "" 