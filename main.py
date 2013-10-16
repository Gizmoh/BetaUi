import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.core.window import Window


class row(BoxLayout):
	nombre = ObjectProperty(None)
	codigo = ObjectProperty(None)
	cantidad = ObjectProperty(None)
	close = ObjectProperty(None)
	contador = 1

class CBoton (Button):
	nombre = ""
	codigo = ""


class Interfaz(BoxLayout):
	boton = CBoton()
	lulbel = Label(text = "TEST")
	test = True
	contador = 0
	X = 0
	lista = []



	def __init__(self,**kwargs):
		super(Interfaz, self).__init__(**kwargs)
		caja = ObjectProperty(None)
		txt = ObjectProperty(None)
		grilla = ObjectProperty(None)
		self.btn = ObjectProperty(None)
		self.boton.ident = "test01"
		for i in range (50):
			Q = CBoton()
			Q.nombre = "derp"+str(i)
			Q.text = Q.nombre
			Q.codigo = str(19*i)
			Q.bind(on_press = self.addStuff)
			self.grilla.add_widget(Q)
			self.grilla.bind(minimum_width=self.grilla.setter('width'))


	def addStuff(interfaz,self):
		temp = row()
		temp.nombre.text = (self.text)
		temp.codigo.text = (self.codigo)
		temp.close.bind(on_press= interfaz.removeStuff)
		for tmp in interfaz.lista:
			if tmp.nombre.text == self.text:
				tmp.contador = tmp.contador + 1
				tmp.cantidad.text = str(tmp.contador)
				interfaz.test = False
		if interfaz.test == True:
			interfaz.lista.append(temp)
			interfaz.caja.add_widget(temp)
			interfaz.caja.bind(minimum_height=interfaz.caja.setter('height'))
		interfaz.test = True

	def removeStuff(interfaz,self):
		self.parent.contador = self.parent.contador - 1
		self.parent.cantidad.text = str(self.parent.contador)
		if self.parent.contador == 0:
			interfaz.caja.remove_widget(self.parent)
			interfaz.lista.remove(self.parent)


def Check(self):
	if self.lista.__contains__(self.text)==True:
		pass

class BetaUiApp(App):
	def build(self):
		return Interfaz()


if __name__ =='__main__':
	BetaUiApp().run()
