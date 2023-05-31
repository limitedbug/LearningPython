def edad():
    edad1 = input("Introduce tu edad");
    if edad1.isdigit():
        print("Tu edad es: %s" % edad1)
    else:
        print("Lo que introduciste no es un numero!");
        edad();

edad()