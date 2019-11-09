"""P7E5 VICTORIA PEÑAS
Escribe un programa que te pida una frase y una vocal,
y pase estos datos como parámetro a una función que se
encargará de cambiar todas las vocales de la frase por
la vocal seleccionada. Devolverá la función la frase
modificada, y el programa principal la imprimirá:"""
def cambiarVocales(f,v):
    for i in f:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            print(v, end="")
        else:
            print(i, end="")
    return frase
frase=str(input("Escribe una frase: "))
vocal=str(input("Dime una vocal: "))
print("La frase ahora es: ", end="")
cambiarVocales(frase,vocal)
