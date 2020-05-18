from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from AccountSettingsScreen import AccountSettingsScreen

class UserScreen(Screen):
    lendtakebtn = ObjectProperty(None)
    settingbtn = ObjectProperty(None)
    givebackbtn = ObjectProperty(None)
    searchbtn = ObjectProperty(None)

    def GetToSettings(self):
        app = App.get_running_app()
        if not app.root.has_screen("account settings screen"):
            app.root.add_widget(AccountSettingsScreen())
        Window.size = (400, 360)
        app.root.current = "account settings screen"

