from mapa import Mapa
from robot import Robot
from moneda import Moneda
from prueba import cargar_mapa , cargar_instrucciones
import time 

de = int(input("Ingrese el numero del archivo que desea abrir " '\n' "1. mapas/mapa1.txt" '\n'))
if de == 1 :
	nombre = "mapas/mapa1.txt"
des = int(input("Ingrese el numero del archivo de las instrucciones " '\n' "1. instrucciones/instrucciones1.txt" '\n'))
if des == 1:
	inst = "instrucciones/instrucciones1.txt"


lista_mapa = cargar_mapa(nombre)
lsita_instrucciones = cargar_instrucciones(inst)

for y in range(len(lista_mapa[0])): #alto
	for x in range(lista_mapa): #ancho
		if lista_mapa [y][x] == '*':
			robot = Robot(x, y)
			robot.colocar_en_mapa(mapa)
			mapa.asignar_robot(robot)
		elif int(lista_mapa[y][x]) > 0:
			for i in range(int(lista_mapa[y][x])):
				moneda = Moneda(x, y)
				mapa.poner_moneda(moneda)

for i in lsita_instrucciones:

	if i == 'MOVE':
		robot.mover()
	elif i == 'ROTATE':
		robot.rotar()
	else:
		robot.recoger()

	print ("Monedas que recoger: " + mapa.contar_monedas())
	print ("Tus monedas: " + robot.monedas)
	print (' ')

	print (mapa.dibujar())
	time.sleep (0.2)