# -*- coding: utf-8 -*-

import kivy
import controller
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window


class row(BoxLayout):
	nombre = ObjectProperty(None)
	codigo = ObjectProperty(None)
	cantidad = ObjectProperty(None)
	close = ObjectProperty(None)
	add = ObjectProperty(None)
	precioU = ObjectProperty(None)
	precioT = ObjectProperty(None)
	contador = 1
	precio = ""

class CBoton (Button):
	nombre = ""
	codigo = ""
	precio = ""


class Interfaz(BoxLayout):
	lista = []


	def __init__(self,**kwargs):
		super(Interfaz, self).__init__(**kwargs)
		caja = ObjectProperty(None)
		txt = ObjectProperty(None)
		grilla = ObjectProperty(None)
		self.btn = ObjectProperty(None)
		products = controller.get_products()
		for fila in products:
			Q = CBoton()
			Q.nombre = fila[0]
			Q.text = fila[0]
			Q.codigo = fila[1]
			Q.precio = fila[2]
			Q.bind(on_press = self.addRow)
			self.grilla.add_widget(Q)
			self.grilla.bind(minimum_width=self.grilla.setter('width'))


	def addRow(interfaz,self):
		test = True
		temp = row()
		temp.nombre.text = (self.text)
		temp.codigo.text = (self.codigo)
		temp.precioU.text = str(self.precio)
		temp.precio = self.precio
		temp.precioT.text = str(self.precio*temp.contador)
		temp.close.bind(on_press= interfaz.removeStuff)
		temp.add.bind(on_press = interfaz.moarStuff)
		for tmp in interfaz.lista:
			if tmp.nombre.text == self.text:
				tmp.contador = tmp.contador + 1
				tmp.cantidad.text = str(tmp.contador)
				tmp.precioT.text = str(self.precio*tmp.contador)
				test = False
		if test == True:
			interfaz.lista.append(temp)
			interfaz.caja.add_widget(temp)
			interfaz.caja.bind(minimum_height=interfaz.caja.setter('height'))
		test = True

	def moarStuff(interfaz, self):
		self.parent.contador = self.parent.contador +1
		self.parent.cantidad.text = str(self.parent.contador)
		self.parent.precioT.text = str(self.parent.precio*self.parent.contador)

	def removeStuff(interfaz,self):
		self.parent.contador = self.parent.contador - 1
		self.parent.cantidad.text = str(self.parent.contador)
		self.parent.precioT.text = str(self.parent.precio*self.parent.contador)
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