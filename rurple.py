from mapa import Mapa
from robot import Robot
from monedas import Moneda
from prueba import cargar_mapa , cargar_instrucciones
import time 

de = int(input("Ingrese el numero del archivo que desea abrir " '\n' "1. mapas/mapa2.txt" '\n'))
if de == 1 :
	nombre = "mapas/mapa2.txt"
des = int(input("Ingrese el numero del archivo de las instrucciones " '\n' "1. instrucciones/instrucciones2.txt" '\n'))
if des == 1:
	inst = "instrucciones/instrucciones2.txt"

lista_mapa = cargar_mapa(nombre)
lista_instrucciones = cargar_instrucciones(inst)

ancho = len(lista_mapa[0])
alto = len(lista_mapa)
mapa = Mapa(ancho, alto)

for y in range(alto): 
	for x in range(ancho): 
		if lista_mapa [y][x] == '*':
			robot = Robot(x, y)
			robot.colocar_en_mapa(mapa)
			mapa.asignar_robot(robot)
		elif int(lista_mapa[y][x]) > 0:
			for i in range(int(lista_mapa[y][x])):
				moneda = Moneda(x, y)
				mapa.poner_moneda(moneda)

for i in lista_instrucciones:

	if i == 'MOVE':
		robot.mover()
	elif i == 'ROTATE':
		robot.rotar()
	else:
		robot.recoger()

	print (mapa.dibujar())
	time.sleep (0.2)

