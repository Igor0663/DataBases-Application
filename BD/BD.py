from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

from LoginScreen import LoginScreen
from LendTakeScreen import LendTakeScreen
from UserScreen import UserScreen
from AdminScreen import AdminScreen 


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.login = None
        self.rig = None


class BDApp(App):
    def build(self):
        return MyScreenManager(transition = NoTransition())



if __name__ == "__main__":
   Window.size = (300, 160)
   BDApp().run()