"""P7E5 VICTORIA PEÑAS
Escribe un programa que te pida una frase y una vocal, y pase estos datos
como parámetro a una función que se encargará de cambiar todas las vocales
de la frase por la vocal seleccionada. Devolverá la función la frase
modificada, y el programa principal la imprimirá:"""

def convertirFrase(texto,letra):
    frase=texto.replace("a",letra)
    frase=frase.replace("e",letra)
    frase=frase.replace("i",letra)
    frase=frase.replace("o",letra)
    frase=frase.replace("u",letra)
    return print(frase)

frase=str(input("Dime un texto: "))
vocal=str(input("Dime una vocal: "))
while vocal!="a" and vocal!="e" and vocal!="i" and vocal!="o" and vocal!="u":
    vocal=str(input("Dime una vocal correcta: "))

convertirFrase(frase,vocal)
