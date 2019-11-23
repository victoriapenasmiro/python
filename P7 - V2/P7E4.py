"""P7E4 VICTORIA PEÑAS
Escribe un programa que pida una frase, y le pase como parámetro
a una función dicha frase. La función debe sustituir todos los
espacios en blanco de una frase por un asterisco, y devolver el
resultado para que el programa principal la imprima por pantalla"""

def sustituirEspacios(texto):
    texto=texto.replace(" ","*")
    print(texto)

frase=str(input("dime una frase y sustituiré los espacios por un *: "))
sustituirEspacios(frase)
