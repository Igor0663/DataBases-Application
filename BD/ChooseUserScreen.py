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
from DbAccessFunctions import Login
from DbAccessFunctions import GetUsers




class ChooseUserScreen(Screen):
    bckbtn = ObjectProperty(Button)
    usrsel = ObjectProperty(Spinner)
    login  = StringProperty('')

    def __init__(self,**kwargs):
        super(ChooseUserScreen, self).__init__(**kwargs)
        self.usrsel.values = GetUsers()

    def UpdateData(self, login):
        self.login = login
    
    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "opcje administratora"
        self.ClearInput()
    
  #  def SubmitNewUsr(self):
  #      app = App.get_running_app()
  #      ChangeDep(app.root.login, self.login, self.depsel.text)
  #      screen = app.root.get_screen("ustawienia konta")
  #      screen.UpdateData(self.login)
  #      Window.size = (400, 360)
  #      app.root.current = "ustawienia konta"
  #      self.ClearInput()

    def ClearInput(self):
        self.usrsel.text = "Wybierz uzytkownika"


