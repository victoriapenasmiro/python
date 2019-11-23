"""P7E10 VICTORIA PEÑAS
Escribe un programa que te pida una palabra o número,
pase por parámetro estos datos a una función, y ésta te diga si
es o no palíndroma o capicúa. El programa principal imprimirá el
resultado de la función"""

def comprobarPalindroma(texto):
    if texto==texto[::-1]:
        res="Es palíndroma o capicua"
    else:
        res="No es palíndroma o capicua"
    return print(f"{texto} {res}")

frase=input("Dime una palabra o un número y comprobaré si es\
palíndromo o capicua: ")
comprobarPalindroma(frase)
