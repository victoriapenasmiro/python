"""P6E9 VICTORIA PEÑAS
Escribe un programa que te pida nombres de personas y sus números de teléfono.
Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina
escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan
los nombres y números de teléfono tiene esta estructura[[nombre1, telef1],
[nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas."""
agenda=[]
nombre=str(input("Dame un nombre: "))
tel=int(input("Dame el teléfono: "))
while nombre!="S":
    agenda.append([nombre,": ",tel])
    nombre=str(input("Dame un nombre: "))
    if nombre!="S":
        tel=int(input("Dame el teléfono: "))
#Al poner "in range identifico los elementos de la lista con indices"
print("Los nombres y teléfonos de la agenda son:")
for i in range(len(agenda)-1):
    for j in range(len(agenda[i])):
        print (agenda[i][j], end="")
   print ("")
#Otra opcion:
# Al NO poner in range en el subbucle coge los valores de la lista,
#no lo coge como si fueran los indices
#for i in range(len(agenda)):
 #   for j in agenda[i]:
  #      print (j, end="")
   # print ("")
