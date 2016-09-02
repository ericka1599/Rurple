class Mapa ():
	def __init__ (self, ancho, alto):
		self.largo = largo
		self.ancho = ancho
		self.moneda = []
		slef.robot = None


	def asignar_robot (self, robot):
		self.robot = robot
	
	def contar_moneda (self, moneda):
		self.moneda.append(moneda)

	def dibujar_mapa (self):
		resultado = ""
		for y in range(self.altura):
			for x in range(self.ancho):
				if moneda.x == x and moneda.y == y:
					resultado += moneda 
				elif robot.x == x and robot.y == y:
					resultado += robot 
				else:
					resultado += " "

			resultado += "\n"

	def contar_moneda (self):
		conteo = 0 
		for y in range(self.altura):
			for x in range(self.ancho):
				if moneda.y == y and moneda.x == x:
					encontrado = True 
					conteo += 1
					break 
			return conteo 

	def quitar_moneda (self):
		for y in range(self.altura):
			for x in range(self.ancho):
				if encontrado == True :
					self.x and self.y += " "

	def 