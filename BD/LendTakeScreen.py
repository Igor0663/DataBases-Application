from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class LendTakeScreen(Screen):
    logcont = ObjectProperty(None)
    pwdcont = ObjectProperty(None)
    namecont = ObjectProperty(None)
    snamecont = ObjectProperty(None)
    depcont = ObjectProperty(None)
    rigcont = ObjectProperty(None)

    logbtn = ObjectProperty(None)
    pwdbtn = ObjectProperty(None)
    namebtn = ObjectProperty(None)
    snamebtn = ObjectProperty(None)
    depbtn = ObjectProperty(None)
    rigbtn = ObjectProperty(None)

    bckbtn = ObjectProperty(None)