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

class UserLayout(GridLayout):
    def __init__(self, **kwargs):
        super(UserLayout,self).__init__(**kwargs)
        self.cols = 2;
        self.rows = 2;
        self.row_force_default = False
        self.row_default_height = 80

        self.options = []
        self.options.append( Button(text="Wypożycz/pobierz sprzęt") )
        self.options.append( Button(text="Ustawienia konta") )
        self.options.append( Button(text="Oddaj sprzęt") )
        self.options.append( Button(text="Przeglądaj sprzęt") )
        for i in self.options:
            self.add_widget(i)


class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self.add_widget(UserLayout())

