class Robot(object):
	def __init__ (self, x, y):
		self.x = medir_ancho
		self.y = medir_alto
		self.moneda = 0
		self.direccion = 0
		self.mapa = None 

	def colocar_en_mapa (self, mapa):
		self.mapa = mapa

	def  rotar (self):
		if self.direccion = (self.direccion + 1) % 4


	def dibujar (self):
		if self.direccion == 0:
			return '↑'
		elif self.direccion == 1:
			return '→'
		elif self.direccion == 2:
			return '←'
		else:
			return '↓'

	def recoger_monedas (self):
		cont = 0
		encontrado = False 
		for y in range(self.altura):
			for x in range(self.ancho):
				if moneda.x == x and moneda.y == y:
					if robot.x == x and robot.y == y:
						encontrado = True 
						cont += moneda 

	def mover (self):
		if self.rotacion == 0:
			self.y -= 1
			if self.y < 0:
				self.y = 0
		elif self.rotacion == 1:
			self.x += 1 
			if self.x > 79 :
				self.x = 79
		elif self.rotacion == 2:
			self.y += 1 
			if self.y > 49 :
				self.y = 49
		else :
			self.x -= 1
			if self.x < 0:
				self.x = 0



