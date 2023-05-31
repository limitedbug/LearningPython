lista = [0, "1", 1.5, [1,2], {3: "efe", "efe": 3}]

print(lista)
for n in lista:
    print(n) # aqui estoy mostrando con un loop, todo el contenido de la lista
# PUEDO MOSTRAR TODOS LOS ELEMENTOS DE LA LISTA SIN UN BUCLE SOLO USANDO POSICIONES :
# saltos 0 1 2 3 4  si pongo el salto en 2  mostrara 0 2 4 
print(lista[0:5:2])
# posiciones negativas puede darnos lo mismo de derecha a izquierda
print("Posicion negativa -1 donde obtenemos el objeto mas especifico pos(3)\"%s\" " % lista[-1][3])
print("Aqui muestro la posicion 3 del array, la cual contiene otro array y muestro la pos 0: %d y pos 1: %d" % (lista[3][0], lista[3][1]))
print("Aca la posicion 4 un objeto y puedo pedir una parte del mismo pos(3)\"%s\" y pos(efe) \"%d\"" % (lista[4][3], lista[4]["efe"]))

# append es para añadir solo 1
# extend es para añadir varios a la vez
# len(lista) longitud
# remove elimina el dato en si no su posicion
# pop este si elimina por su indice
# index me da la posicion de lo que busco
# count es para contar las veces que se repite un dato en la lista
# reverse nos permite revertir una lista

#split para separar
# join para concatenar 