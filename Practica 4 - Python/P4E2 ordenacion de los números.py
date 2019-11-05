#este programa informa de la ordenacion de los números
num1=int(input("Por favor, indique el primer número\n"))
num2=int(input("Por favor, indique el segundo número\n"))
num3=int(input("Por favor, indique el tercer número\n"))
num4=int(input("Por favor, indique el cuarto número\n"))
num5=int(input("Por favor, indique el quinto número\n"))
if num1<=num2 and num2<=num3 and num3<=num4 and num4<=num5:
    print("La ordenacion de los números introducidos es creciente.")
elif num1>=num2 and num2>=num3 and num3>=num4 and num4>=num5:
    print("La ordenacion de los números introducidos es decreciente.")
else:
    print("Los números están desordenados.")
