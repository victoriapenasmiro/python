"""P6E7 VICTORIA PEÑAS
Escribe un programa que pida un número (límite) y luego te pida números
hasta que la suma de los números introducidos supere el límite inicial.
El programa termina escribiendo la lista de números."""
i=0
li_num=[]
num_lim=int(input("Escribe límite: "))
while i<num_lim:
    valor=int(input("Escribe un valor: "))
    li_num.append(valor)
    i=i+valor
print(f"El límite a superar es {num_lim}.La lista creada es ", end="")
for j in li_num:
    if j!=li_num[-1]:
        print(j,end=", ")
    else:
        print(j,end="")
print(f" ya que la suma de estos números es:{i}")
