from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from AccountSettingsScreen import AccountSettingsScreen

class AdminScreen(Screen):
    lendtakebtn = ObjectProperty(Button)
    settingbtn  = ObjectProperty(Button)
    givebackbtn = ObjectProperty(Button)
    searchbtn   = ObjectProperty(Button)
    usermgbtn   = ObjectProperty(Button)
    gearmgbtn   = ObjectProperty(Button)

    def GetToSettings(self):
        app = App.get_running_app()
        screen = app.root.get_screen("ustawienia konta")
        screen.UpdateData(app.root.login)
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"

    def GetToMgUsers(self):
        app = App.get_running_app()
        screen = app.root.get_screen("wybierz uzytkownika")
        screen.UpdateData()
        Window.size = (400, 360)
        app.root.current = "wybierz uzytkownika"
