from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

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

    def GetBack(self):
        app = App.get_running_app()
        if app.root.rig == "czlonek_kola":
            Window.size = (400, 160)
            app.root.current = "opcje czlonka kola"
        elif app.root.rig == "administrator":
            Window.size = (400, 360)
            app.root.current = "opcje administratora"
        