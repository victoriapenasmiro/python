"""P7E8 VICTORIA PEÑAS
Escribe un programa que pida una frase, y pase la frase como parámetro
a una función que debe eliminar los espacios en blanco (compactar la frase).
El programa principal imprimirá por pantalla el resultado final.
+ info en https://stackoverrun.com/es/q/2136639"""
def eliminarEspacios(seq):
    return seq.replace(" ","")
frase=str(input("Escribe una frase y eliminaré los espacios: "))
print(eliminarEspacios(frase))
