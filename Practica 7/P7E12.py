"""P7E13 VICTORIA PEÑAS
Escribir un programa que lea una frase, y pase ésta como parámetro a una
función que debe contar el número de palabras que contiene. Debe imprimir el
programa principal el resultado. Asumir que cada palabra está separada por
un solo blanco:
a-Asumir que cada palabra está separada por un solo blanco.
b-No se sabe cómo están separadas las palabras. Pueden estar separadas por
más de un blanco o por signos de puntuación."""
import re,string
def leerFrase(valor):
    li=[]
    palabra=""
    valor=re.sub('[%s]' % re.escape(string.punctuation),'',valor)#reemplaza
                                            #los signos de puntuacion por nada
    for i in valor:
        if i !=" ":
            palabra+=i
            ult_letra=i
        if i == " " and ult_letra !=" ":#(valor(i)-1) == '[%s]':#si hay un espacio y justo antes una letra --> no funciona
            li.append(palabra)
        elif i==valor[-1]:
            li.append(palabra)
    for k in range(len(li)):
        vueltas=k
    if vueltas==0:
        vuetas=1
    return print("el número de palabras de la frase es",vueltas+1)
frase=str(input("Dime una frase: "))
leerFrase(frase)
