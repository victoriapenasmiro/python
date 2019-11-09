biblioteca=[]#los pongo "a mano" los libros lo suyo seria tener un menu y que
#los fuera pidiendo
libro1=["3i33isbn","intro a la programación","pepe","juan"]
libro2=["3i4ufisbn","programación en python","vicky","jose","david","laura"]

biblioteca.append(libro1)
biblioteca.append(libro2)

##recorremos e imprimimos la información

for i in range(len(biblioteca)):
    print("================================")
    print ("esta es la información guardada del libro ",i)
    for j in biblioteca[i]:
        print(j,end=" ")
