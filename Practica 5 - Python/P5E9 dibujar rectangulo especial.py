#este programa dibuja un rectangulo
anchura=int(input("dame la anchura:\n"))
altura=int(input("dame la altura:\n"))
print ("*"*anchura)
for i in range(1,altura-2):
    print ("*"," "*(anchura-4),"*")
print ("*"*anchura)
