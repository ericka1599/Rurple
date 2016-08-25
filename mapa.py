class Mapa ():
	def __init__ (self, largo, ancho, monedas):
		self.largo = largo
		self.ancho = ancho
		self.monedas = monedas

	def cargar_mapa (nombre):
		mapa = open(nombre, "r")
		lista_mapa = [ ]

		for i in mapa:
			lista_mapa.append(list(i.strip()))
		mapa.close()
		return lista_mapa

	def cargar_instrucciones (inst):
		ins = open(inst, "r")
		lista_instrucciones = []

		for i in ins:
			lista_instrucciones.append(list(i.strip()))
		ins.close()
		return lista_instrucciones
	
	def medir_largo (self):
		largo = len(lista_mapa[0,0])
		self.largo = largo

	def medir_ancho (self):
		ancho = len(lista_mapa/largo)
		self.ancho = ancho

	def encontrar_monedas (self):
		moneda_encontrada = False 
		monedas_encontradas = 0
		for i in lista_mapa:
			if i != 0:
				moneda_encontrada = True
				monedas_encontradas += 1

	def  


