from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from AccountSettingsScreen import AccountSettingsScreen

class AdminScreen(Screen):
    lendtakebtn = ObjectProperty(None)
    settingbtn  = ObjectProperty(None)
    givebackbtn = ObjectProperty(None)
    searchbtn   = ObjectProperty(None)
    usermgbtn   = ObjectProperty(None)
    gearmgbtn   = ObjectProperty(None)

    def GetToSettings(self):
        app = App.get_running_app()
        screen = app.root.get_screen("ustawienia konta")
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"