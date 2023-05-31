# en pocas palabras, su funcionamiento es que el bucle exterior controla las veces que se repite el ciclo exterior
# cuando un ciclo exterior se cumple, tiene que esperar al ciclo interior para completar un ciclo
# para continuar con el suyo y asi sucesivamente
ele = 1;
for i in range(0, 11):
    
    for f in range(0, 9):
        
        print(ele)
        ele+=1;
    