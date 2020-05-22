from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView

from DbAccessFunctions import UsableEquipmentKind
from DbAccessFunctions import Equipment
from ChooseUserScreen import SelectableLabel
from ChooseUserScreen import SelectableRecycleBoxLayout


class EqpList(RecycleView):
    ChosenElement = ObjectProperty(SelectableLabel)
    def __init__(self, **kwargs):
        super(EqpList, self).__init__(**kwargs)
        eqpdata = Equipment()
        self.data=[{'text':x[0]} for x in eqpdata]

class ManageEquipScreen(Screen):

	typesel = ObjectProperty(Spinner)
	kindsel = ObjectProperty(Spinner)
	srch = ObjectProperty(TextInput)
	srchbtn = ObjectProperty(Button)
	eqplst = ObjectProperty(EqpList)
	addusbtn = ObjectProperty(Button)
	addunusbtn = ObjectProperty(Button)
	adduskdbtn = ObjectProperty(Button)
	addunuskdbtn = ObjectProperty(Button)
	delbtn = ObjectProperty(Button)
	modbtn = ObjectProperty(Button)
	bckbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(ManageEquipScreen, self).__init__(**kwargs)
		self.typesel.values = ["Wybierz typ","sprzęty zużywalne", "sprzęty niezużywalne"]


	def UpdateData(self):
		eqpdata = Equipment()
		self.eqplst.data=[{'text':x[0]} for x in eqpdata]

	def GetBack(self):
		app = App.get_running_app()
		Window.size = (400, 360)
		app.root.current = "opcje administratora"
		self.ClearInput()
	
	def ClearInput(self):
		self.typesel.text = "Wybierz typ"


class AddUsableEqpScreen(Screen):
#	eqpname = StringProperty(TextInput)
	amount = StringProperty(TextInput)
	kindsel = ObjectProperty(Spinner)
	bckbtn = ObjectProperty(Button)
	confbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(AddUsableEqpScreen, self).__init__(**kwargs)
		self.kindsel.values = UsableEquipmentKind()

	def SubmitAdding(self):
		app = App.get_running_app()
		value = int(self.amount)
		AddEqpUs(app.root.login, self.eqpname, value, self.kindsel.text)
		screen = app.root.get_screen("zarzadzaj sprzetem")
		screen.UpdateData()
		Window.size = (400, 360)
		app.root.current = "zarzadzaj sprzetem"
		self.ClearInput()

	def GetBack(self):
		app = App.get_running_app()
		Window.size = (400, 360)
		app.root.current = "zarzadzaj uzytkownikami"
		self.ClearInput()

	def ClearInput(self):
		self.kindsel.text = "Wybierz rodzaj"
