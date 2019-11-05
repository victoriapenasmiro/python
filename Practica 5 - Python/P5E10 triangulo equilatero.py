"""P5E10 VICTORIA PEÑAS
Escribe un programa que pida la altura de un
triángulo y lo dibuje de la siguiente manera:"""

altura=int(input("dame la altura:\n"))

for i in range(altura+1):
    print (" "*(altura-i)+"*"*(i*2-1))


"""intentos fallidos"""
#for i in range(1,altura*2,2):
 #   espacios=altura-i

#print(" "*altura+"*")
#for i in range(altura):
 #   espacios=altura-i
  #  i=i+1
   # print(" "*espacios+"*"*i+"*"*i)

#for i in range(-1,altura*2-1,2):
 #   if i/2!=0:
  #      i=i+1
   # print(" "*i+"*"*i+"*")
