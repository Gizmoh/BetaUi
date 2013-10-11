import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.core.window import Window


class Interfaz(BoxLayout):
	pass


class BetaUiApp(App):
	def build(self):
		return Interfaz()


if __name__ =='__main__':
	BetaUiApp().run()