from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from DbAccessFunctions import GetUserData
from DbAccessFunctions import ChangeLogin
from DbAccessFunctions import ChangePwd
from DbAccessFunctions import GetRights
from DbAccessFunctions import ChangeName
from DbAccessFunctions import ChangeSname

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

    login = ObjectProperty(None)

    def UpdateData(self, login):
        self.login = login
        app = App.get_running_app()
        user_data = GetUserData(self.login)
        self.logcont.text = user_data[2]
        self.namecont.text = user_data[1]
        self.snamecont.text = user_data[0]
        self.depcont.text = user_data[3]
        self.rigcont.text = user_data[4]
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
        screen = app.root.get_screen("zmiana loginu")
        screen.UpdateData(self.login)
        Window.size = (400, 160)
        app.root.current = "zmiana loginu"

    def ChangePwd(self):
        app = App.get_running_app()
        screen = app.root.get_screen("zmiana hasla")
        screen.UpdateData(self.login)
        Window.size = (400, 200)
        app.root.current = "zmiana hasla"

    def ChangeName(self):
        app = App.get_running_app()
        screen = app.root.get_screen("zmiana imienia")
        screen.UpdateData(self.login)
        Window.size = (400, 160)
        app.root.current = "zmiana imienia"
    
    def ChangeSname(self):
        app = App.get_running_app()
        screen = app.root.get_screen("zmiana nazwiska")
        screen.UpdateData(self.login)
        Window.size = (400, 160)
        app.root.current = "zmiana nazwiska"

class ChangeLoginScreen(Screen):
    newlog = ObjectProperty(None)
    newlog2 = ObjectProperty(None)
    accbtn = ObjectProperty(None)
    bckbtn = ObjectProperty(None)

    login = ObjectProperty(None)

    def UpdateData(self, login):
            self.login = login

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def SubmitNewLogin(self):
        if(self.newlog.text == self.newlog2.text and len(self.newlog.text) >= 6):
            app = App.get_running_app()
            ChangeLogin(self.login, self.newlog.text)
            if self.login == app.root.login:
                app.root.login = self.newlog.text
            self.UpdateData(self.newlog.text)
            screen = app.root.get_screen("ustawienia konta")
            screen.UpdateData(self.login)
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

    login = ObjectProperty(None)

    def UpdateData(self, login):
            self.login = login

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def SubmitNewPwd(self):
        app = App.get_running_app()
        if(GetRights(self.login, self.oldpwd.text) and  self.newpwd.text == self.newpwd2.text and len(self.newpwd.text) >= 6):
            ChangePwd(self.login, self.oldpwd.text, self.newpwd.text)
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

    login = ObjectProperty(None)

    def UpdateData(self, login):
            self.login = login

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def SubmitNewName(self):
        if(self.newname.text == self.newname2.text and len(self.newname.text) >= 3):
            app = App.get_running_app()
            ChangeName(app.root.login, self.login, self.newname.text)
            screen = app.root.get_screen("ustawienia konta")
            screen.UpdateData(self.login)
            Window.size = (400, 360)
            app.root.current = "ustawienia konta"
            self.ClearInput()

    def ClearInput(self):
        self.newname.text = ""
        self.newname2.text = "" 

class ChangeSnameScreen(Screen):
    newsname = ObjectProperty(None)
    newsname2 = ObjectProperty(None)
    accbtn = ObjectProperty(None)
    bckbtn = ObjectProperty(None)

    login = ObjectProperty(None)

    def UpdateData(self, login):
            self.login = login

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def SubmitNewSname(self):
        if(self.newsname.text == self.newsname2.text and len(self.newsname.text) >= 3):
            app = App.get_running_app()
            ChangeSname(app.root.login, self.login, self.newsname.text)
            screen = app.root.get_screen("ustawienia konta")
            screen.UpdateData(self.login)
            Window.size = (400, 360)
            app.root.current = "ustawienia konta"
            self.ClearInput()

    def ClearInput(self):
        self.newsname.text = ""
        self.newsname2.text = "" 