from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from DbAccessFunctions import GetUserData
from DbAccessFunctions import Login
from DbAccessFunctions import GetUsersNamesLogins
from DbAccessFunctions import DeleteUser

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior


        
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    pass

class SelectableLabel(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        rv.ChosenElement = self

class UserList(RecycleView):
    ChosenElement = ObjectProperty(SelectableLabel)
    def __init__(self, **kwargs):
        super(UserList, self).__init__(**kwargs)
        usrdata = GetUsersNamesLogins()
        self.data=[{'text':x[0],'UserLogin':x[1]} for x in usrdata]

class ChooseUserScreen(Screen):
    bckbtn = ObjectProperty(Button)
    delbtn = ObjectProperty(Button)
    modbtn = ObjectProperty(Button)
    addbtn = ObjectProperty(Button)
    usrlst = ObjectProperty(UserList)
    

    def __init__(self,**kwargs):
        super(ChooseUserScreen, self).__init__(**kwargs)

    def UpdateData(self):
        usrdata = GetUsersNamesLogins()
        self.usrlst.data=[{'text':x[0],'UserLogin':x[1]} for x in usrdata]
    
    def GetToMod(self):
        app = App.get_running_app()
        login = self.usrlst.data[self.usrlst.ChosenElement.index]['UserLogin']
        screen = app.root.get_screen("ustawienia konta")
        screen.UpdateData(login)
        Window.size = (400, 360)
        app.root.current = "ustawienia konta"
        self.ClearInput()

 #       ChosenLogin = self.usrlst.data[self.usrlst.ChosenElement.index]['UserLogin']


    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "opcje administratora"
    
    def GetToAdd(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "dodaj uzytkownika"

    def GetToDel(self):
        app = App.get_running_app()
        login = self.usrlst.data[self.usrlst.ChosenElement.index]['UserLogin']
        screen = app.root.get_screen("usun uzytkownika")
        screen.UpdateData(login)
        Window.size = (400, 360)
        app.root.current = "usun uzytkownika"
        self.ClearInput()


    def ClearInput(self):
        pass


class DeleteUserScreen(Screen):
    nobtn = ObjectProperty(Button)
    yesbtn = ObjectProperty(Button)
    userlogin = StringProperty('')
    
    def __init__(self,**kwargs):
        super(DeleteUserScreen, self).__init__(**kwargs)

    def UpdateData(self, login):
        self.userlogin = login
  
    def SubmitDeletion(self):
        app = App.get_running_app()
        DeleteUser(app.root.login, self.userlogin)
        screen = app.root.get_screen("wybierz uzytkownika")
        screen.UpdateData()
        Window.size = (400, 360)
        app.root.current = "wybierz uzytkownika"

    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "wybierz uzytkownika"
        






