from mapa import medir_alto
from mapa import medir_ancho 
import time 
class Robot(object):
	def __init__ (self, x, y):
		self.x = x
		self.y = y
		self.monedas = 0
		self.direccion = 'UP'
		self.mapa = None 

	def colocar_en_mapa (self, mapa):
		self.mapa = mapa

	def posicion (x, y):
		resultado = (" " * ancho) * y
		resultado += " " * x + "*"
		resultado += " " + ancho * (alto - (y + 1))
		return resultado

		steps = 19 
		for i in range (steps):
			time.sleep(0.2)
			print(posicion(5 + i, i)) 

	def mostrar_robot (self, direccion):
		if self.direccion == 'UP':
			return '↑'
		elif self.direccion == 'RIGHT':
			return '→'
		elif self.direccion == 'LEFT':
			return '←'
		else:
			return '↓'

