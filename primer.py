
from ntpath import realpath


print("efe")
#Para notas #####

#en python no se define el tipo de variable
booleano = True;
Entero = 1;
Entero2 = 2;
Real = 1.34;
Alfanumerico = "efe1";

#%d para entero
# %f para flotante/real
# %s para alfanumericos/strings
# %d tambien funciona para boleanos
# Se tiene que usar % variable para decirle que lo identifique
# En los reales puedes especificar cuantos decimales puede tener
print("Variable entera %d" % Entero)
print("Variable flotante %1.2f" % Real)
print("Variable Alfanumerico %s"  % Alfanumerico)
print("Variable booleanos %d" % booleano)

# Es facil poner 2 o mas variables solo listandolos
# concatenar se puede tambien hacer como en c debido a que esta basado en el mismo "texto"+variable+"texto"
print("Variable entera %d Variable flotante %1.2f Variable entera2 %d" % (Entero, Real, Entero2))