# Format es como una combinacion entre replace y la concatenacion de variables
# los numeros pueden seguir creciendo dependiendo de cuantas variables pondras en el format
texto1 = "efe"
texto2 = "efe2"
print("texto {0} texto2 {1}".format(texto1, texto2))
print('texto {} texto2 {}'.format(texto1,texto2))
#hay diferentes formas, puedes poner indices, no poner nada (pero en esta tienes que poner los datos respectivos)
# de igual manera puedes asignar variables a, b a= texto1 b = texto2
#si pones un indice o una asignacion puedes poner repetidamente cada uno

print("texto {0} texto2 {1} texto {0} texto2 {1}".format(texto1, texto2))


#en un format puedes hacer que sea centrado, a la derecha o izquierda
# ^ centro
# > derecha
# < izquierda
# :pos num el num hara que ocupe esa cantidad de caracteres para el espaciado

print("Centrado".center(70, "*"))
print("| {0:>20} | {1:>20}".format(texto1, texto2))