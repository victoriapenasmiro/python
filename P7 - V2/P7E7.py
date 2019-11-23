"""P7E7 VICTORIA PEÑAS
Escribe un programa que lea una frase, y la pase como
parámetro a un procedimiento. El procedimiento contará
el número de vocales (de cada una) que aparecen, y lo
imprimirá por pantalla."""

def leerFrase(texto):
    a=texto.count("a")+texto.count("A")
    e=texto.count("e")+texto.count("E")
    i=texto.count("i")+texto.count("I")
    o=texto.count("o")+texto.count("O")
    u=texto.count("u")+texto.count("U")
    print(f"Hay: {a} vocales a,{e} vocales e,{i} vocales i,{o} vocales\
o y {u} vocales u.")

frase=str(input("Dime una frase y te diré cuantas vocales contiene:\n"))
leerFrase(frase)
