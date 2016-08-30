class Mapa ():
	def __init__ (self, ancho, alto):
		self.largo = largo
		self.ancho = ancho
		self.monedas = []
		slef.robot = None


	def asignar_robot (self, robot):
		self.robot = robot
	
	def contar_monedas (self, moneda):
		self.monedas.append(moneda)

	def dibujar_mapa (self):
		resultado = ""
		for y in range(self.altura):
			for x in range(self.ancho):
				if monedas.x == x and monedas.y == y:
					resultado = mone

	def crear (self, mapa, monedas, robot):
		mapa = Mapa (len(lista_mapa[0])) , len(lista_mapa)
		for y in range(len(lista_mapa)):
			for x in range(len(lista_mapa[y])):
				if lista_mapa [x][y] == "*":
					robot = Robot (x, y)
					mapa.poner_robot(Robot)
				elif lista_mapa [x][y] == "0":
					return " "
				else:
					cantidad = int(lista_mapa[y][x])
					for i in range(cantidad):
						moneda = Moneda(x, y)
						mapa.agregar_moneda(Moneda)

