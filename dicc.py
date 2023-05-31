# dicc.keys() regresa todas las claves  en el diccionario
# dicc.items() regresa una lista completa de elementos del dicc
# por lo que veo, es lo mismo que un objeto+
services = {'ftp': 21, 'ssh':22,'smtp': "3", 'http': 80}
print(str(services.keys())+"\n")
print(str(services.items()))

print(services['ftp'])