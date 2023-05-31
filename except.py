
def edad():
    try:
        edad1 = int(input("Introduce tu edad"))
        print("tu edad es: %s" % edad1)
    except:
        print("Lo que introdujiste no fue un numero")
        edad()

edad()
# se puede limitar el except a el tipo de error "except <error>"
