"""P6E3 VICTORIA PEÑAS
Escribe un programa que pida notas y los guarde en una lista.
Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
El programa termina escribiendo la lista de notas."""

li_notas=[]
i=float(input("Escribre una nota:"))
while i>=0 and i<=10:
    li_notas.append(i)
    i=float(input("Escribre una nota:"))
print("Las notas que has Escrito son ",li_notas)
