## Bucle while infinito
i = 1

# while True:
#     us = str(input("Ingresa un numero para sacar su multiplicacion o \"end\" para terminar el programa"))
#     if us != "end":
        
#         while i <= 10:
#             print("{} x {} = {}".format(int(us), i, (int(us))*i))
#             i = i+1
#         i = 1;
#     else: 
#         break;

## bucle for in

lista = ["pedro", "Juanito", "san pablo", "tu madre"]
for nombre in lista:
    print(nombre)



## bucle while con la misma lista
i = 0;
while i < len(lista):
    print(lista[i])
    i = i+1;

#impresion de 10 num en un bucle 
for num in range(0, 11):
    print(num);

pot = 0;
while pot >= 0 and pot <11:
    print(pot)
    pot = pot+1