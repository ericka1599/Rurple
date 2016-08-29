from rurple import cargar_mapa
class Mapa ():
	def __init__ (self, ancho, alto):
		self.largo = largo
		self.ancho = ancho
		self.monedas = []
		slef.robot = None
	
	def medir_ancho (self):
		ancho = len(lista_mapa[0,0])
		self.ancho = ancho

	def medir_alto (self):
		alto = len(lista_mapa/ancho)
		self.largo = largo

	def encontrar_monedas (self):
		moneda_encontrada = False 
		monedas_encontradas = 0
		for i in lista_mapa:
			if i != 0:
				moneda_encontrada = True
				monedas_encontradas += 1
				if moneda_encontrada == True:
					return i

	def mostrar_mapa (self):











def crear (mapa, monedas, robot):
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
