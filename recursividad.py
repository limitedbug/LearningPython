def clave(intentos = 1):
    respuesta = input("Ingresa la contraseña\n");
    if(respuesta != "abc123"):
        if(intentos < 3):
            intentos += 1;
            print("Clave incorrecta, Intenta denuevo\n")
            clave(intentos)
        else:
            print("Usuario Bloqueado!\n");
    else:
        print("Contraseña Correcta");

clave()