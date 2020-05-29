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
from ChooseUserScreen import SelectableLabel
from ChooseUserScreen import SelectableRecycleBoxLayout
from DbAccessFunctions import UsOrders
from DbAccessFunctions import UnUsOrders

class ChooseTypeOrderBrowseScreen(Screen):
	usordbtn = ObjectProperty(Button)
	unusordbtn = ObjectProperty(Button)
	bckbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(ChooseTypeOrderBrowseScreen, self).__init__(**kwargs)

	def GetToUsOrd(self):
		app = App.get_running_app()
		Window.size = (600, 400)
		screen = app.root.get_screen("przegladaj zamowienia zuzywalne")
		screen.UpdateData()
		app.root.current = "przegladaj zamowienia zuzywalne"

	def GetToUnUsOrd(self):
		pass
		app = App.get_running_app()
		Window.size = (600, 400)
		screen = app.root.get_screen("przegladaj zamowienia niezuzywalne")
		screen.UpdateData()
		app.root.current = "przegladaj zamowienia niezuzywalne"

	def GetBack(self):
		app = App.get_running_app()
		Window.size = (400, 360)
		app.root.current = "opcje administratora"



class UsOrdersList(RecycleView):
    ChosenElement = ObjectProperty(SelectableLabel)
    def __init__(self, **kwargs):
        super(UsOrdersList, self).__init__(**kwargs)
        orddata = UsOrders()
        self.data=[{'text':x[0], 'numer': x[1]} for x in orddata]

class UnUsOrdersList(RecycleView):
    ChosenElement = ObjectProperty(SelectableLabel)
    def __init__(self, **kwargs):
        super(UnOrdersList, self).__init__(**kwargs)
        orddata = UnUsOrders()
        self.data=[{'text':x[0], 'numer': x[1]} for x in orddata]

class BrowseUsOrdersScreen(Screen):
	ordlst = ObjectProperty(UsOrdersList)
	detailbtn = ObjectProperty(Button)
	bckbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(BrowseUsOrdersScreen, self).__init__(**kwargs)
		orddata = UsOrders()
		self.ordlst.data=[{'text':x[0], 'numer': x[1]} for x in orddata]

	def GetBack(self):
		app = App.get_running_app()
		Window.size = (400, 150)
		app.root.current = "wybor typu zamowienia przegladanie"
	
	def UpdateData(self):
		orddata = UsOrders()
		self.ordlst.data=[{'text':x[0], 'numer': x[1]} for x in orddata]
		self.ordlst.refresh_from_data()

class BrowseUnUsOrdersScreen(Screen):
	ordlst = ObjectProperty(UsOrdersList)
	detailbtn = ObjectProperty(Button)
	bckbtn = ObjectProperty(Button)

	def __init__(self,**kwargs):
		super(BrowseUnUsOrdersScreen, self).__init__(**kwargs)
		orddata = UnUsOrders()
		self.ordlst.data=[{'text':x[0], 'numer': x[1]} for x in orddata]

	def GetBack(self):
		app = App.get_running_app()
		Window.size = (400, 150)
		app.root.current = "wybor typu zamowienia przegladanie"
	
	def UpdateData(self):
		orddata = UnUsOrders()
		self.ordlst.data=[{'text':x[0], 'numer': x[1]} for x in orddata]
		self.ordlst.refresh_from_data()