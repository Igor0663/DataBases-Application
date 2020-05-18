from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.properties import StringProperty

from LoginScreen import LoginScreen
from AccountSettingsScreen import AccountSettingsScreen
from UserScreen import UserScreen
from AdminScreen import AdminScreen 


class MyScreenManager(ScreenManager):
    login = StringProperty('')
    rig = StringProperty('')


class BDApp(App):
    def build(self):
        return MyScreenManager(transition = NoTransition())



if __name__ == "__main__":
   Window.size = (300, 160)
   BDApp().run()