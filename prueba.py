from rurple import cargar_mapa, cargar_instrucciones 

de = int(input("Ingrese el numero del archivo que desea abrir " '\n' "1. mapas/mapa1.txt" '\n'))
if de == 1 :
	nombre = "mapas/mapa1.txt"
des = int(input("Ingrese el numero del archido de las instrucciones " '\n' "1. instrucciones/instrucciones1.txt" '\n'))
if des == 1:
	inst = "instrucciones/instrucciones1.txt"

#an = len(lista_mapa[0][0])

#alt = len(lista_mapa/an)

print (cargar_mapa(nombre))
print (cargar_instrucciones(inst))
print (lista_mapa)