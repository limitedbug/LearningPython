
opcion = 0;
opcionG = 0;
bandera = "";
def menu():
    print("Opciones:\n[0]Multiplicar\n[1]Dividir\n[2]Sumar\n[3]Restar\n")
    opcion = int(input("Ingresa un numero para seleccionar una opcion\n"))
    if opcion < 0 or opcion > 3:
        print(1)
        return "";
    return opcion;


def operaciones(opcion, num1, num2):
    
    if opcion == 0:
        return "Multiplicacion hecha: %d" % (num1*num2)
    elif opcion == 1:
        return "Division hecha: %d" % (num1/num2)
    elif opcion == 2:
        return "Suma hecha: %d" % (num1+num2)
    else: 
        return "Resta hecha: %d" % (num1-num2)





def main():
    opcionG = menu();
    if opcionG == "":
        return "s"

    num1 = int(input("Ingresa un numero entero"));
    num2 = int(input("Ingresa otro numero entero"));

    print(operaciones(opcionG, num1, num2))

    bandera = str(input("Desea continuar? y/n"))
    return bandera;




# se pueden poner descripciones a las funciones con """
# 
#   y asi"""
while True:
    stop = main();
    if stop == "y":
        pass;
    elif stop == "n":
        break;
    else:
        print("Opcion no valida, Reiniciando Programa")

# en las funciones para definir que estamos pidiendo una lista y un diccionario
# tenemos que poner * o ** respectivamente de cada uno
