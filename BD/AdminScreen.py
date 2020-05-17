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


class AdminGrid(GridLayout):
    def __init__(self, **kwargs):
        super(AdminGrid,self).__init__(**kwargs)
        self.cols = 2;
        self.rows = 3;
        self.row_force_default = False
        self.row_default_height = 60

        self.options = []
        self.options.append( Button(text="Wypożycz/pobierz sprzęt") )
        self.options.append( Button(text="Ustawienia konta") )
        self.options.append( Button(text="Oddaj sprzęt") )
        self.options.append( Button(text="Przeglądaj sprzęt") )
        self.options.append( Button(text="Zarządzaj sprzętem") )
        self.options.append( Button(text="Zarządzaj użytkownikami") )
        for i in self.options:
            self.add_widget(i)

class AdminLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(AdminLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 0
        self.grid = AdminGrid()
        self.button = Button(text="Przeglądaj zamówienia", size_hint = (1, 0.25) )

        self.add_widget(self.grid)
        self.add_widget(self.button)


class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminScreen, self).__init__(**kwargs)
        self.add_widget(AdminLayout())