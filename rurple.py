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

def crear (mapa, monedas, robot):
	mapa = Mapa (len(lista_mapa[0])) , len(lista_mapa)
	for y in range(len(lista_mapa)):
		for x in range(len(lista_mapa[y])):
			if lista_mapa [x][y] = "*":
				robot = Robot (x, y)
				robot 

		


