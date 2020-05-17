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



class LoginGrid(GridLayout):
    def __init__(self, **kwargs):
        super(LoginGrid, self).__init__(**kwargs)
        self.cols = 2;
        self.rows = 2;
        self.row_force_default = False
        self.row_default_height = 40

        self.log = TextInput(multiline = False)
        self.pwd = TextInput(multiline = False, password = True)

        self.add_widget(Label(text="login"))
        self.add_widget(self.log)
        self.add_widget(Label(text="hasło"))
        self.add_widget(self.pwd)

class LoginLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.grid = LoginGrid()
        
        self.button = Button(text ="Zaloguj się")
        self.button.bind(on_press=partial(self.login_try, self.button))        
        self.add_widget(self.grid)
        self.add_widget(self.button)

    def login_try(self, instance, *args):
        cnx = mysql.connector.connect(user='sudo', password='xbxbpun', database='bd_projekt')
        cur = cnx.cursor(buffered=True)
        args = [self.grid.log.text, self.grid.pwd.text, '']
        result_args = cur.callproc('logowanie', args)
        #print(result_args[2])
        if result_args[2] == 'czlonek_kola':
            Window.size = (400, 160)
            app= App.get_running_app()
            app.root.current = 'opcje członka koła'
        elif result_args[2] == 'administrator':
            Window.size = (400, 360)
            app= App.get_running_app()
            app.root.current = 'opcje administratora'
        cnx.close()



class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.add_widget(LoginLayout())