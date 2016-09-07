from mapa import Mapa
from robot import Robot
from monedas import Monedas

ancho = len(mapa[0][0])
alto = 

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

def mostrar_mapa ():
	for i in range(lista_mapa):
		if i == 0:
			return " "
		elif i != 0 :
			return i 
			monedas_encontradas.append[i]
		elif i == "*":
			return Robot(mostrar_robot)



		


