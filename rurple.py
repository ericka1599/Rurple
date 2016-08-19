def Cargar_mapa (nombre):
	mapa = open(nombre, "r")
	lista = [ ]

	for i in mapa:
		lista.append(list(i.strip()))
	return lista

	mapa.close()