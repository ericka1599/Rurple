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

	def dibujar (self):
		resultado = ""
		for y in range(self.altura):
			for x in range(self.ancho):
<<<<<<< HEAD
				if x == self.robot.x and y == self.robot.y:
					resultado =+ self.robot.dibujar()
				elif self.contar_monedas(x, y) > 0:
					resultado =+ self.contar_monedas(x, y)
=======
				if self.contar_monedas (x, y) > 0:
					resultado += self.contar_monedas(x, y) 
				elif self.robot.x == x and self.robot.y == y:
					resultado += self.robot.dibujar_robot 
>>>>>>> origin/master
				else:
					resultado += " "

			resultado += "\n"

	def contar_moneda (self, x, y):
		conteo = 0 
		for moneda in self.monedas:

			if moneda.y == y and moneda.x == x:
				conteo += 1
<<<<<<< HEAD
				break 
		return conteo 

	def remover (self, x, y):
=======
		return conteo 

	def quitar_moneda (self):

>>>>>>> origin/master
		coincidencia = -1
		for indice in range(len(self.monedas)):
			moneda = self.monedas[indice]
			if moneda.x == x and moneda.y == y:
<<<<<<< HEAD
				coincidencia = indice
				break

		if coincidencia >= 0:
			self.monedas.pop (coincidencia)
=======
				coincidencia = indice 
				break 

		if indice >= 0:
			self.monedas.pop(indice)
>>>>>>> origin/master
