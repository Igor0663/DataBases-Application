from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from DbAccessFunctions import GetDepartments
from DbAccessFunctions import GetRights


class AddUserScreen(Screen):
    newname = ObjectProperty(TextInput)
    newsname = ObjectProperty(TextInput)
    newlogin = ObjectProperty(TextInput)
    newpwd = ObjectProperty(TextInput)
    newpwd2 = ObjectProperty(TextInput)
    confbtn = ObjectProperty(Button)
    bckbtn = ObjectProperty(Button)
    depsel = ObjectProperty(Spinner)
    rigsel = ObjectProperty(Spinner)

    def __init__(self,**kwargs):
        super(AddUserScreen, self).__init__(**kwargs)
        self.depsel.values = GetDepartments()
        self.rigsel.values = GetRights()
    
    def GetBack(self):
        app = App.get_running_app()
        screen = app.root.get_screen("wybierz uzytkownika")
        screen.UpdateData()
        Window.size = (400, 360)
        app.root.current = "wybierz uzytkownika"
        self.ClearInput()
    
    def SubmitNewUsr(self):
        app = App.get_running_app()
        if(self.newpwd.text == self.newpwd2.text):
            newuser = AddNewUser(app.root.login, self.newname.text, self.newsname.text, self.newlogin.text, self.newpwd.text, self.depsel.text, self.rigsel.text)
            if newuser != None:
                screen = app.root.get_screen("wybierz uzytkownika")
                screen.UpdateData()
                Window.size = (400, 360)
                app.root.current = "wybierz uzytkownika"
                self.ClearInput()

    def ClearInput(self):
        self.depsel.text = "Wybierz dzial"