"""P6E5 VICTORIA PEÑAS
Escribe un programa que te pida números cada vez más grandes
y que se guarden en una lista. Para acabar de escribir los
números, escribe un número que no sea mayor que el anterior.
El programa termina escribiendo la lista de números:"""
li_num=[]
nummayor=int(input("Escribe un número: "))
i=(nummayor-1)
while i<nummayor:
   li_num.append(nummayor)
   i=nummayor
   nummayor=int(input(f"Escribe un número mayor que {nummayor}:"))
print("Los números que has escrito son: ",end="")
for j in li_num:
    if j!=li_num[-1]:#hago referencia al último elemento de la lista
        print(j,end=", ")
    else:
        print(j)
