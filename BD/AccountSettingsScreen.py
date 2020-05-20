from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from DbAccessFunctions import GetUserData
from DbAccessFunctions import ChangeLogin
from DbAccessFunctions import ChangePwd
from DbAccessFunctions import Login
from DbAccessFunctions import ChangeName
from DbAccessFunctions import ChangeSname
from DbAccessFunctions import GetDepartments
from DbAccessFunctions import ChangeDep
from DbAccessFunctions import GetRights
from DbAccessFunctions import ChangeRig

class AccountSettingsScreen(Screen):
    logcont = ObjectProperty(Label)
    pwdcont = ObjectProperty(Label)
    namecont = ObjectProperty(Label)
    snamecont = ObjectProperty(Label)
    depcont = ObjectProperty(Label)
    rigcont = ObjectProperty(Label)

    logbtn = ObjectProperty(Button)
    pwdbtn = ObjectProperty(Button)
    namebtn = ObjectProperty(Button)
    snamebtn = ObjectProperty(Button)
    depbtn = ObjectProperty(Button)
    rigbtn = ObjectProperty(Button)

    bckbtn = ObjectProperty(Button)

    login = StringProperty('')

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
        if app.root.login == self.login:
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
    
    def ChangeDep(self):
        app = App.get_running_app()
        screen = app.root.get_screen("zmiana dzialu")
        screen.UpdateData(self.login)
        Window.size = (400, 160)
        app.root.current = "zmiana dzialu"
    def ChangeRig(self):
        app = App.get_running_app()
        screen = app.root.get_screen("zmiana uprawnien")
        screen.UpdateData(self.login)
        Window.size = (400, 160)
        app.root.current = "zmiana uprawnien"

class ChangeLoginScreen(Screen):
    newlog = ObjectProperty(TextInput)
    newlog2 = ObjectProperty(TextInput)
    accbtn = ObjectProperty(Button)
    bckbtn = ObjectProperty(Button)

    login = StringProperty('')

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
    oldpwd = ObjectProperty(TextInput)
    newpwd = ObjectProperty(TextInput)
    newpwd2 = ObjectProperty(TextInput)
    accbtn = ObjectProperty(Button)
    bckbtn = ObjectProperty(Button)

    login = StringProperty('')

    def UpdateData(self, login):
            self.login = login

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def SubmitNewPwd(self):
        app = App.get_running_app()
        if(Login(self.login, self.oldpwd.text) and  self.newpwd.text == self.newpwd2.text and len(self.newpwd.text) >= 6):
            ChangePwd(self.login, self.oldpwd.text, self.newpwd.text)
            Window.size = (400, 360)
            app.root.current = "ustawienia konta"
            self.ClearInput()

    def ClearInput(self):
        self.oldpwd.text = ""
        self.newpwd.text = ""
        self.newpwd2.text = ""  

class ChangeNameScreen(Screen):
    newname = ObjectProperty(TextInput)
    newname2 = ObjectProperty(TextInput)
    accbtn = ObjectProperty(Button)
    bckbtn = ObjectProperty(Button)

    login = StringProperty('')

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
    newsname = ObjectProperty(TextInput)
    newsname2 = ObjectProperty(TextInput)
    accbtn = ObjectProperty(Button)
    bckbtn = ObjectProperty(Button)

    login = StringProperty('')

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


class ChangeDepScreen(Screen):
    accbtn = ObjectProperty(Button)
    bckbtn = ObjectProperty(Button)
    depsel = ObjectProperty(Spinner)
    login  = StringProperty('')

    def __init__(self,**kwargs):
        super(ChangeDepScreen, self).__init__(**kwargs)
        self.depsel.values = GetDepartments()

    def UpdateData(self, login):
        self.login = login
    
    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()
    
    def SubmitNewDep(self):
        app = App.get_running_app()
        ChangeDep(app.root.login, self.login, self.depsel.text)
        screen = app.root.get_screen("ustawienia konta")
        screen.UpdateData(self.login)
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def ClearInput(self):
        self.depsel.text = "Wybierz dzial"

class ChangeRigScreen(Screen):
    accbtn = ObjectProperty(Button)
    bckbtn = ObjectProperty(Button)
    rigsel = ObjectProperty(Spinner)
    login = StringProperty('')

    def __init__(self,**kwargs):
        super(ChangeRigScreen, self).__init__(**kwargs)
        self.rigsel.values = GetRights()

    def UpdateData(self, login):
        self.login = login
    
    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()
    
    def SubmitNewRig(self):
        app = App.get_running_app()
        ChangeRig(app.root.login, self.login, self.rigsel.text)
        if(app.root.login == self.login):
            app.root.rig = self.rigsel.text
        screen = app.root.get_screen("ustawienia konta")
        screen.UpdateData(self.login)
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

    def ClearInput(self):
        self.rigsel.text = "Wybierz uprawnienia"