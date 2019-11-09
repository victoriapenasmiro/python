"""P6E6 VICTORIA PEÑAS
Escribe un programa que pida primero dos números (máximo y mínimo)
y que después te pida números intermedios. Para terminar de escribir
números, escribe un número que no esté comprendido entre los dos valores
iniciales. El programa termina escribiendo la lista de números."""
min=int(input("Escribe un número: "))
max=int(input(f"Escribe un número mayor que {min}: "))
while max<=min:
    max=int(input(f"{max} no es mayor que {min}. Vuelve a probar: "))
li_num=[]
i=int(input(f"Escribe un número entre {min} y {max}: "))
while i>min and i<max:
    li_num.append(i)
    i=int(input(f"Escribe un número entre {min} y {max}: "))
print(f"Los números situados entre {min} y {max} que has escrito son: ",end="")
for j in li_num:
    if j!=li_num[-1]:
        print(j,end=", ")
    else:
        print(j)
