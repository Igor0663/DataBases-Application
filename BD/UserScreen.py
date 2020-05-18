from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class UserScreen(Screen):
    lendtakebtn = ObjectProperty(None)
    settingbtn = ObjectProperty(None)
    givebackbtn = ObjectProperty(None)
    searchbtn = ObjectProperty(None)


