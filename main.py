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
from kivy.event import EventDispatcher


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
	kek = 0

	def __init__(self,**kwargs):
		#Inicializacion de la interfaz
		super(Interfaz, self).__init__(**kwargs)
		#Definicion de Variables
		listaB = []
		kek = 1
		caja = ObjectProperty(None)
		txt = ObjectProperty(None)
		grilla = ObjectProperty(None)
		discount = ObjectProperty(None)
		total = ObjectProperty(None)
		save = ObjectProperty(None)
		imprimir = ObjectProperty(None)
		send = ObjectProperty(None)
		money = ObjectProperty(None)
		self.discount.bind(focus = self.addDiscount)
		products = controller.get_products()
		users = controller.get_users()
		#Ingreso de usuarios al Spinner
		for i in users:
			listaB.append(i[0])
		self.txt.text = listaB[0]
		self.txt.values = listaB
		#Ingreso de productos a la lista deslizante
		for fila in products:
			Q = CBoton()
			Q.background_color = 1,1,1,(kek%2+0.5)
			kek = kek+1
			Q.nombre = fila[0]
			Q.text = fila[0]
			Q.codigo = fila[1]
			Q.precio = fila[2]
			Q.bind(on_press = self.addRow)
			self.grilla.add_widget(Q)
			self.grilla.bind(minimum_width=self.grilla.setter('width'))



	def addRow(interfaz,self):#Agrega productos a la grilla
		test = True
		temp = row()
		temp.nombre.text = (self.text)
		temp.codigo.text = (self.codigo)
		temp.precioU.text = ("$ "+str(self.precio))
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
				setPrice(interfaz)
		if test == True:
			interfaz.lista.append(temp)
			interfaz.caja.add_widget(temp)
			interfaz.caja.bind(minimum_height=interfaz.caja.setter('height'))
			setPrice(interfaz)
		test = True

	def moarStuff(interfaz, self):#Agrega mas productos a elementos de la grilla, mediante el boton
		self.parent.contador = self.parent.contador +1
		self.parent.cantidad.text = str(self.parent.contador)
		self.parent.precioT.text = str(self.parent.precio*self.parent.contador)
		setPrice(interfaz)

	def removeStuff(interfaz,self):#Reduce y elimina productos de la grilla
		self.parent.contador = self.parent.contador - 1
		self.parent.cantidad.text = str(self.parent.contador)
		self.parent.precioT.text = str(self.parent.precio*self.parent.contador)
		if self.parent.contador == 0:
			interfaz.caja.remove_widget(self.parent)
			interfaz.lista.remove(self.parent)
		setPrice(interfaz)

	def addDiscount(interfaz,self, value):
		temp = float(interfaz.money.text)
		if temp == 0:
			pass
		if value == False:
			if float(self.text) > 0:
				interfaz.total.text = str(float(interfaz.money.text) - ((float(interfaz.money.text)*float(self.text))/100))
			if float(self.text) == 0:
				interfaz.total.text = interfaz.money.text

	def calcDiscount(self):
		self.addDiscount(self.discount,False)


def setPrice(interfaz):#Sets prices
	temp = 0
	#print(interfaz.money.text)
	for i in interfaz.lista:
		temp = temp + (float(i.precioT.text))
	interfaz.money.text = str(temp)
	interfaz.calcDiscount()


def Check(self):
	if self.lista.__contains__(self.text)==True:
		pass

class BetaUiApp(App):
	def build(self):
		return Interfaz()


if __name__ =='__main__':
	BetaUiApp().run()