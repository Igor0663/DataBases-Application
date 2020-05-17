from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import TransitionBase, NoTransition
import mysql.connector 

from LoginScreen import LoginScreen
from UserScreen import UserScreen
from AdminScreen import AdminScreen 


sm = ScreenManager(transition = NoTransition() )
sm.add_widget(LoginScreen(name='ekran logowania'))
sm.add_widget(UserScreen(name='opcje członka koła'))
sm.add_widget(AdminScreen(name='opcje administratora'))


class BDApp(App):
    def build(self):
        return sm



if __name__ == "__main__":
   Window.size = (300, 160)
   BDApp().run()