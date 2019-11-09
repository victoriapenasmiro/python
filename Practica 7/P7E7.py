"""P7E7 VICTORIA PEÑAS
Escribe un programa que lea una frase, y la pase como parámetro
a un procedimiento. El procedimiento contará el número de vocales
(de cada una) que aparecen, y lo imprimirá por pantalla.
+ info sobre esta funcion en
https://www.tutorialspoint.com/python/string_count.htm"""
def leerFrase(frase):
    if "a" in frase:
        sub="a"
        print("El número de vocales \"a\" que se han encontrado son"\
          ,frase.count(sub))
    if "e" in frase:
        sub="e"
        print("El número de vocales \"e\" que se han encontrado son"\
          ,frase.count(sub))
    if "i" in frase:
        sub="i"
        print("El número de vocales \"i\" que se han encontrado son"\
          ,frase.count(sub))
    if "o" in frase:
        sub="o"
        print("El número de vocales \"o\" que se han encontrado son"\
          ,frase.count(sub))
    if "u" in frase:
        sub="u"
        print("El número de vocales \"u\" que se han encontrado son"\
          ,frase.count(sub))
frase=str(input("Escribe una frase y haré un recuento de las vocales\
que se han utilizado: "))
leerFrase(frase)
