"""P7E8 VICTORIA PEÑAS
Escribe un programa que pida una frase, y pase la frase como parámetro
a una función que debe eliminar los espacios en blanco (compactar la frase).
El programa principal imprimirá por pantalla el resultado final."""

def eliminarEspacios(texto):
    texto=texto.split()
    for i in texto:
        print (i,end="")
    return

frase=str(input("Dime una frase y la conectenaré:\n"))
eliminarEspacios(frase)
