from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from DbAccessFunctions import GetRights


class LoginScreen(Screen):
    log = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def LoginTry(self):
        app= App.get_running_app()
        rights = GetRights(self.log.text, self.pwd.text)
        if rights != None:
            app.root.login = self.log.text
            app.root.rig = rights
            screen = app.root.get_screen("ustawienia konta")
            screen.UpdateData()
        if rights == 'czlonek_kola':
            Window.size = (400, 160)
            app.root.current = 'opcje czlonka kola'
        elif rights == 'administrator':
            Window.size = (400, 360)
            app.root.current = 'opcje administratora'