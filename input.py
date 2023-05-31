# en py 2 es raw_input() pero como tengo la 3 es solo input()

# Declaramos variables vacias

edad = 0;
estatura = 0.0;
nombres = "";
apellidos = "";

edad = int(input("Introduce tu edad"));
estatura = float(input("Introduce tu estatura"));
nombres = input("Introduce tus nombres")
apellidos = input("Introduce tus apellidos")

print("Bienvenido %s %s, tu edad es %d y tu estatura es %f" %(nombres, apellidos, edad, estatura))
