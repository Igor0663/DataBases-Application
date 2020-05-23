from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView

from DbAccessFunctions import UsableEquipmentKind
from DbAccessFunctions import UnUsableEquipmentKind
from DbAccessFunctions import Equipment
from DbAccessFunctions import AddEqpUs
from DbAccessFunctions import AddEqpUnUs
from DbAccessFunctions import AddEqpUsKind
from ChooseUserScreen import SelectableLabel
from ChooseUserScreen import SelectableRecycleBoxLayout


class EqpList(RecycleView):
    ChosenElement = ObjectProperty(SelectableLabel)
    def __init__(self, **kwargs):
        super(EqpList, self).__init__(**kwargs)
        eqpdata = Equipment()
        self.data=[{'text':x[0]} for x in eqpdata]

class ManageEquipScreen(Screen):

	kind = ListProperty([])
	srch = ObjectProperty(TextInput)
	srchbtn = ObjectProperty(Button)
	eqplst = ObjectProperty(EqpList)
	addusbtn = ObjectProperty(Button)
	addunusbtn = ObjectProperty(Button)
	adduskdbtn = ObjectProperty(Button)
	addunuskdbtn = ObjectProperty(Button)
	deluskdbtn = ObjectProperty(Button)
	delunuskdbtn = ObjectProperty(Button)
	advbtn = ObjectProperty(Button)
	delbtn = ObjectProperty(Button)
	modbtn = ObjectProperty(Button)
	bckbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(ManageEquipScreen, self).__init__(**kwargs)
		self.UpdateData()

	def GetToAddUs(self):
		app = App.get_running_app()
		Window.size = (400, 360)
		screen = app.root.get_screen("dodaj sprzet zuzywalny")
		screen.UpdateData()
		app.root.current = "dodaj sprzet zuzywalny"
		self.ClearInput()

	def GetToAddUnUs(self):
		app = App.get_running_app()
		Window.size = (400, 150)
		app.root.current = "dodaj sprzet niezuzywalny"
		self.ClearInput()

	def GetToAddUsKind(self):
		app = App.get_running_app()
		Window.size = (400, 100)
		app.root.current = "dodaj rodzaj sprzetu zuzywalnego"
		self.ClearInput()

	def GetToAdv(self):
		app = App.get_running_app()
		Window.size = (400, 300)
		app.root.current = "zaawansowane zarzadzanie sprzetem"
		self.ClearInput()


	def UpdateData(self):
		eqpdata = Equipment()
		self.eqplst.data=[{'text':x[0]} for x in eqpdata]
		self.kind = UnUsableEquipmentKind()

	def GetBack(self):
		app = App.get_running_app()
		Window.size = (400, 360)
		app.root.current = "opcje administratora"
		self.ClearInput()
	
	def ClearInput(self):
		self.ids.typesel.text = "Wybierz typ"
		self.ids.kindsel.text = "Wybierz rodzaj"
		self.srch.text = ""

class AddUsableEqpScreen(Screen):
	eqpname = ObjectProperty(TextInput)
	amount = ObjectProperty(TextInput)
	kind = ListProperty([])
	bckbtn = ObjectProperty(Button)
	confbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(AddUsableEqpScreen, self).__init__(**kwargs)
		self.UpdateData()

	def SubmitAdding(self):
		app = App.get_running_app()
		value = int(self.amount.text)
		AddEqpUs(app.root.login, self.eqpname.text, value, self.kindsel.text)
		screen = app.root.get_screen("zarzadzaj sprzetem")
		screen.UpdateData()
		Window.size = (900, 600)
		app.root.current = "zarzadzaj sprzetem"
		self.ClearInput()

	def UpdateData(self):
		self.kind = UsableEquipmentKind()

	def GetBack(self):
		app = App.get_running_app()
		screen = app.root.get_screen("zarzadzaj sprzetem")
		screen.UpdateData()
		Window.size = (900, 600)
		app.root.current = "zarzadzaj sprzetem"
		self.ClearInput()

	def ClearInput(self):
		self.ids.kindsel.text = "Wybierz rodzaj"
		self.eqpname.text = ""
		self.amount.text = ""

class AddUnUsableEqpScreen(Screen):
	eqpname = ObjectProperty(TextInput)
	kind = ListProperty([])
	bckbtn = ObjectProperty(Button)
	confbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(AddUnUsableEqpScreen, self).__init__(**kwargs)
		self.UpdateData() 

	def SubmitAdding(self):
		app = App.get_running_app()
		AddEqpUnUs(app.root.login, self.eqpname.text, self.kindsel.text)
		screen = app.root.get_screen("zarzadzaj sprzetem")
		screen.UpdateData()
		Window.size = (900, 600)
		app.root.current = "zarzadzaj sprzetem"
		self.ClearInput()

	def GetBack(self):
		app = App.get_running_app()
		screen = app.root.get_screen("zarzadzaj sprzetem")
		screen.UpdateData()
		Window.size = (900, 600)
		app.root.current = "zarzadzaj sprzetem"
		self.ClearInput()

	def ClearInput(self):
		self.ids.kindsel.text = "Wybierz rodzaj"
		self.eqpname.text = ""
	
	def UpdateData(self):
		self.kind = UnUsableEquipmentKind()

class AddUsableEqpKindScreen(Screen):
	kindname = ObjectProperty(TextInput)
	bckbtn = ObjectProperty(Button)
	confbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(AddUsableEqpKindScreen, self).__init__(**kwargs)

	def SubmitAdding(self):
		app = App.get_running_app()
		AddEqpUsKind(app.root.login, self.kindname.text)
		screen = app.root.get_screen("dodaj sprzet zuzywalny")
		screen.UpdateData()
		Window.size = (900, 600)
		app.root.current = "zarzadzaj sprzetem"
		self.ClearInput()

	def GetBack(self):
		app = App.get_running_app()
		screen = app.root.get_screen("zarzadzaj sprzetem")
		screen.UpdateData()
		Window.size = (900, 600)
		app.root.current = "zarzadzaj sprzetem"
		self.ClearInput()

	def ClearInput(self):
		self.kindname.text = ""


class AdvancedEqpScreen(Screen):
	debtusrbtn= ObjectProperty(Button)
	unreturneqpbtn = ObjectProperty(Button)
	unavaileqpbtn = ObjectProperty(Button)
	bckbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(AdvancedEqpScreen, self).__init__(**kwargs)

	def GetBack(self):
		app = App.get_running_app()
		screen = app.root.get_screen("zarzadzaj sprzetem")
		screen.UpdateData()
		Window.size = (900, 600)
		app.root.current = "zarzadzaj sprzetem"
