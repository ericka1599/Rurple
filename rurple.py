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

ancho = 
alto = 

lista_mapa = cargar_mapa(nombre)
lista_instrucciones = cargar_instrucciones(inst)

for y in range(): #alto
	for x in range(): #ancho
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

	for i in ins:
		lista_instrucciones.append(list(i.strip()))
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


	print ("Monedas que recoger: " + mapa.contar_monedas())
	print ("Tus monedas: " + robot.monedas)
	print (' ')

	print (mapa.dibujar())
	time.sleep (0.2)