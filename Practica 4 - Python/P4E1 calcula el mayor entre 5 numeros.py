#Este programa calcula el mayor entre 5 numeros
num1=int(input("Por favor, indique el primer número\n"))
num2=int(input("Por favor, indique el segundo número\n"))
num3=int(input("Por favor, indique el tercer número\n"))
num4=int(input("Por favor, indique el cuarto número\n"))
num5=int(input("Por favor, indique el quinto número\n"))
if num1>=num2 and num1>=num3 and num1>=num4 and num1>=num5:
    print (f"El número más elevando de los que se han introducido es {num1}")
elif num1>=num2 and num1<=num3 and num3>=num4 and num3>=num5:
    print (f"El número más elevando de los que se han introducido es {num3}")
elif num1>=num2 and num1>=num3 and num1<=num4 and num4>=num5:
    print (f"El número más elevando de los que se han introducido es {num4}")
elif num1>=num2 and num1>=num3 and num1>=num4 and num1<=num5:
    print (f"El número más elevando de los que se han introducido es {num5}")
elif num1<=num2 and num2>=num3 and num2>=num4 and num2>=num5:
    print (f"El número más elevando de los que se han introducido es {num2}")
elif num1<=num2 and num2<=num3 and num3>=num4 and num3>=num5:
    print (f"El número más elevando de los que se han introducido es {num3}")
elif num1<=num2 and num2<=num3 and num3<=num4 and num4>=num5:
    print (f"El número más elevando de los que se han introducido es {num4}")
elif num1<=num2 and num2<=num3 and num3<=num4 and num4>=num5:
    print (f"El número más elevando de los que se han introducido es {num4}")
else:
    print (f"El número más elevando de los que se han introducido es {num5}")
    
