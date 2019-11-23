"""P7E11 VICTORIA PEÑAS
Escribe un programa que te pida una frase, y pase la frase como
parámetro a una función. Ésta debe devolver si es palíndroma o no ,
y el programa principal escribirá el resultado por pantalla"""

def comprobarPalindroma(texto):
    texto=texto.split() #aplico este método para eliminar espacios, tabulaciones,
                        #y cualquier hueco vacio
    frase=""
    for i in texto:
        frase+=i
    if frase==frase[::-1]:
        res="Es palíndroma"
    else:
        res="No es palíndroma"
    return print(res)

frase=str(input("Dime una frase y te diré si es palíndroma:\n"))
comprobarPalindroma(frase)
