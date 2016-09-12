class Robot(object):
	def __init__ (self, x, y):
		self.x = ancho
		self.y = alto
		self.monedas = 0
		self.direccion = 0
		self.mapa = None 

	def colocar_en_mapa (self, mapa):
		self.mapa = mapa

	def  rotar (self):
		if self.direccion == 0:
			self.direccion = 1
		elif self.direccion == 1:
			self.direccion = 2
		elif self.direccion == 2:
			self.direccion = 3
		else:
			self.direccion = 0
			
	def dibujar (self):
		if self.direccion == 0:
			return '↑'
		elif self.direccion == 1:
			return '→'
		elif self.direccion == 2:
			return '←'
		else:
			return '↓'

	def recoger (self):
		if self.mapa.contar_monedas(self.x, self.y) > 0:
			self.monedas += 1
			self.mapa.remover(x, y)

	def mover (self):
		if self.rotacion == 0:
			self.y -= 1
			if self.y < 0:
				self.y = 0
		elif self.rotacion == 1:
			self.x += 1 
			if self.x > ancho :
				self.x = ancho
		elif self.rotacion == 2:
			self.y += 1 
			if self.y > alto :
				self.y = alto
		else :
			self.x -= 1
			if self.x < 0:
				self.x = 0



