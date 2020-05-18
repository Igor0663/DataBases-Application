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
        if not app.root.has_screen("account settings screen"):
            app.root.add_widget(AccountSettingsScreen())
        Window.size = (400, 360)
        app.root.current = "account settings screen"