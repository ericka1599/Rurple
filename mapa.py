class Mapa ():
	def __init__ (self, ancho, alto):
		self.alto = alto
		self.ancho = ancho
		self.monedas = []
		self.robot = None


	def asignar_robot (self, robot):
		self.robot = robot
	
	def poner_moneda (self, moneda):
		self.monedas.append(moneda)

	def dibujar_mapa (self):
		resultado = ""
		for y in range(self.altura):
			for x in range(self.ancho):
				if self.contar_monedas (x, y) > 0:
					resultado += self.contar_monedas(x, y) 
				elif self.robot.x == x and self.robot.y == y:
					resultado += self.robot.dibujar_robot 
				else:
					resultado += " "

			resultado += "\n"

	def contar_moneda (self, x, y):
		conteo = 0 
		for moneda in self.moneda:

			if moneda.y == y and moneda.x == x:
				conteo += 1
		return conteo 

	def quitar_moneda (self):

		coincidencia = -1
		for indice in range(len(self.monedas)):
			moneda = self.monedas[indice]
			if moneda.x == x and moneda.y == y:
				coincidencia = indice 
				break 

		if indice >= 0:
			self.monedas.pop(indice)