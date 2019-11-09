"""P6E8 VICTORIA PEÑAS
Escribe un programa que te pida primero un número y luego te pida números
hasta que la suma de los números introducidos coincida con el número inicial.
El programa termina escribiendo la lista de números."""

num_lim=int(input("Escribe límite: "))
li_num=[]
valor=int(input("Escribe un valor: "))
i=0
while (valor+i)>num_lim: #mientras la suma del valor dado con el sumario (i)
                        #sea mayor que el limite, pide otro valor
    valor=int(input(f"{valor} es demasiado grande. Escribe otrovalor: "))
if (valor+i)==num_lim: #Si el primer valor dado es igual al limite imprime lista
    li_num.append(valor)
while (valor+i)<num_lim: #mientras la suma del valor con el sumatorio (i) sea
                        #menor que el limite ejecuta instrucciones
    li_num.append(valor) #inserta el valor en la lista
    i+=valor #recalcula el sumatorio
    valor=int(input("Escribe otro valor: "))#dame otro valor
    if (i+valor)==num_lim: # si la suma del nuevo valor con el acumulado (i)
                            #igual que el limite, inserta el valor en la lista y ejecuta
        li_num.append(valor)
    while (i+valor)>num_lim:# mientras la suma del nuevo valor con el acumulado
                            #(i) sea mayor que el limite, solicita otro valor
        valor=int(input(f"{valor} es demasiado grande. Escribe otro valor: "))
        if (i+valor)==num_lim:#si el nuevo valor dado es igual al limite
                                #inserta en lista y ejecuta.
            li_num.append(valor)
print(f"El límite a alcanzar es {num_lim}. La lista creada es: ",end="")
for j in li_num:
    if j!=li_num[-1]:
        print(j,end=", ")
    else:
        print(j)

    
