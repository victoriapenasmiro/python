#este programa calcula que números entre un rango son impares y cuales pares
num1=int(input("Escribe un número\n"))
num2=int(input(f"Escribe un número mayor a {num1}\n"))
for i in range(num1,num2):
    if i%2==0:
        print(f"El número {i} es par")
    else:
        print(f"El número {i} es impar")
