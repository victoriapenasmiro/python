"""P7E4 VICTORIA PEÑAS
Escribe un programa que pida una frase, y le pase como parámetro
a una función dicha frase. La función debe sustituir todos los
espacios en blanco de una frase por un asterisco, y devolver el
resultado para que el programa principal la imprima por pantalla."""
def sustituirEspacios(frase):
    for i in frase:
        if i==" ":
            print("*",end="")
        else:
            print(i,end="")
    return frase
frase=str(input("Escribe una frase: "))
sustituirEspacios(frase)
