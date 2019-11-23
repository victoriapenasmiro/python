"""P7E12 VICTORIA PEÑAS
Escribir un programa que lea una frase, y pase ésta como parámetro a
una función que debe contar el número de palabras que contiene. Debe
imprimir el programa principal el resultado. Asumir que cada palabra
está separada por un solo blanco:
Asumir que cada palabra está separada por un solo blanco.
No se sabe cómo están separadas las palabras. Pueden estar separadas
por más de un blanco o por signos de puntuación."""
def contarPalabras(texto):
    palabras=texto.split()
    #No es una solucion perfecta porqué el for se queda con la primera
    #lista que ha recibido y no se actualiza con la nueva lista que se
    #declara en el if y sigue dando vueltas. Tendría que programar algo
    #para hacer lo siguiente:mientras el texto contengan algún elemento
    #que no esté en la lista ejecuta
    for i in palabras:
        for j in i:
            if j not in ABECEDARIO:
                texto=texto.replace(j,"")
                palabras=texto.split()
                
    return print(len(palabras))

#CONSTANTE
ABECEDARIO=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",\
            "q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",\
            "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",\
            "W","X","Y","Z"]

frase=str(input("Dime una frase y te diré cuantas palabras contiene:\n"))
contarPalabras(frase)
