class Robot(object):
	def __init__ (self, x, y):
		self.x = medir_ancho
		self.y = medir_alto
		self.monedas = 0
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

	def recoger_monedas (self, x, y):

