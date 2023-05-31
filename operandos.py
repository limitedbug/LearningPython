# Operandores lodicos
# + - * / son los normales
# ** esto es para sacar la potencia
# // esto es para sacar una division pero sin decimales, solo entera
# % modulo, por lo que entendi puede usarse para mas cosas pero entendi que puedo saber si es o no par % 2
# parece ser que este puede ayudar a sacar el decimal de un numero ^^^

#se pueden convertir a un dato usando int, float

tramastr = "2500000777";
Pentera = 0;
PDecimal = 0;

print("trama inicial %s" % tramastr)

Pentera = int(tramastr)/1000 # aqui estoy convirtiendo el string a numero entero y dividiendolo entre mil sacando el numero sin mostrar decimales

PDecimal = int(tramastr) % 1000 # aqui es lo mismo pero aqui solo estoy sacando los decimales de la division entre mil

print("Parte entera: %d Parte decimal: %d" % (Pentera, PDecimal))
print("Todo junto: %d.%d" % (Pentera, PDecimal))