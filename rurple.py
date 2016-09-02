from mapa import dibujar_mapa

de = int(input("Ingrese el numero del archivo que desea abrir " '\n' "1. mapas/mapa1.txt" '\n'))
if de == 1 :
	nombre = "mapas/mapa1.txt"
des = int(input("Ingrese el numero del archivo de las instrucciones " '\n' "1. instrucciones/instrucciones1.txt" '\n'))
if des == 1:
	inst = "instrucciones/instrucciones1.txt"

ancho = len(mapa[0])
for i in range(len(mapa)):
	altura = len(mapa)- (len(mapa) - 1)
	ancho = i / altura

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



print (cargar_mapa(nombre))
print (cargar_instrucciones(inst))

		


