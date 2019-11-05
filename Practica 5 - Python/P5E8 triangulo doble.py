#este programa dibuja un triangulo normal y al reves
altura=int(input("por favor, indica la altura\n"))
for i in range(1,altura+1):
    print ("*"*i)
for j in range(altura-1,0,-1):
    print("*"*j)
