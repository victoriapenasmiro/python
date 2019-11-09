"""P6E1 VICTORIA PEÑAS
Escribe un programa que te pida palabras y las guarde en una lista.
Para terminar de introducir palabras, simplemente pulsa Enter.
El programa termina escribiendo la lista de palabras"""

palabra1=str(input("Escribe una palabra: "))
i=palabra1
maspalabras=[]
while i!="":
    maspalabras.append(i)
    i=str(input("Escribe más palabras: "))
print("Las palabras que has escrito son:",maspalabras)
