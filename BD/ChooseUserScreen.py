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

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior




class ChooseUserScreen(Screen):
    bckbtn = ObjectProperty(Button)
    login  = StringProperty('')

    def __init__(self,**kwargs):
        super(ChooseUserScreen, self).__init__(**kwargs)
#        self.usrlst.values = GetUsers()

    def UpdateData(self, login):
        self.login = login
    
    def GetBack(self):
        app = App.get_running_app()
        Window.size = (400, 360)
        app.root.current = "opcje administratora"
        self.ClearInput()
    
  #  def SubmitNewUsr(self):
  #      app = App.get_running_app()
  #      ChangeDep(app.root.login, self.login, self.depsel.text)
  #      screen = app.root.get_screen("ustawienia konta")
  #      screen.UpdateData(self.login)
  #      Window.size = (400, 360)
  #      app.root.current = "ustawienia konta"
  #      self.ClearInput()

    def ClearInput(self):
        pass
#        self.usrsel.text = "Wybierz uzytkownika"

class UserList(RecycleView):
    usrlst = ObjectProperty(RecycleView)
    def __init__(self, **kwargs):
        super(UserList, self).__init__(**kwargs)
        usrdata = GetUsersNamesLogins()
        self.data=[{'text':x} for x in usrdata]


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
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))
