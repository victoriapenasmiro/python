#este programa calcula el factorial de un número
num=int(input("Indica el número del que quieres conocer el factorial\n"))
factorial=num-1
for i in range(num,0,-1):
    factorial=factorial*i
    print(f"El factorial de {num} es {factorial}")
