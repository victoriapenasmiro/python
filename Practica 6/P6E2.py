"""P6E2 VICTORIA PEÑAS
Escribe un programa que te pida números y los guarde en una lista.
Para terminar de introducir número, simplemente escribe “Salir”.
El programa termina escribiendo la lista de números."""
num1=int(input("Escribe un número: "))
listanum=[]
i=num1
while i!="salir":
    listanum.append(int(i)) #indico que i solo inserte numeros a la lista
    i=input("Escribe otro número: ")
print("Los números que has escrito son:",listanum)
    
