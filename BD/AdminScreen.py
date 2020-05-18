from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class AdminScreen(Screen):
    lendtakebtn = ObjectProperty(None)
    settingbtn  = ObjectProperty(None)
    givebackbtn = ObjectProperty(None)
    searchbtn   = ObjectProperty(None)
    usermgbtn   = ObjectProperty(None)
    gearmgbtn   = ObjectProperty(None)