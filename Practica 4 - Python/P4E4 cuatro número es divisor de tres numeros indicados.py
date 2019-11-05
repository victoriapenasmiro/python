#este programa comprueba 4 números y si el 4 es divisor de los tres primeros
num1=int(input("por favor, escribe el primer número\n"))
num2=int(input("por favor, escribe el segundo número\n"))
num3=int(input("por favor, escribe el tercer número\n"))
num4=int(input("por favor, escribe el cuarto número\n"))
if (num1 or num2 or num3)%num4==0:
    print("El cuarto número indicado es divisor de los tres primeros")
else:
    print("El cuarto número indicado no es divisor de los tres primeros")
