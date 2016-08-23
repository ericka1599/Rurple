from rurple import cargar_mapa, cargar_instrucciones 

nombre = input("Ingrese el nombre del archivo que desea abrir: ")
inst = input("Ingrese el nombre del archido de las insrucciones: ")

print (cargar_mapa(nombre))
print (cargar_instrucciones(inst))