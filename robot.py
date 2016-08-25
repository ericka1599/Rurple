from mapa import medir_alto
from mapa import medir_ancho 
import time 
class Robot():
	def __init__ (self, encendido, direccion, posicion, mapa):
	self.encendido = False 
	self.posicion = posicion 
	self.direccion = direccion 

	def posicion (x, y):
		resultado = (" " * ancho) * y
		resultado += " " * x + "*"
		resultado += " " + ancho * (alto - (y + 1))
		return resultado

		steps = 19 #CREO que aqui hay que poner cuantas instrucciones hay
		for i in range (steps):
			time.sleep(0.2)
			print(posicion(5 + i, i)) #Aqui se puede poner x,y

