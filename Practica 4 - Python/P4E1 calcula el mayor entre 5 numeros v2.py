#Este programa calcula el mayor entre 5 numeros
num1=int(input("Por favor, indique el primer número\n"))
num2=int(input("Por favor, indique el segundo número\n"))
num3=int(input("Por favor, indique el tercer número\n"))
num4=int(input("Por favor, indique el cuarto número\n"))
num5=int(input("Por favor, indique el quinto número\n"))
if num1>num2:
    mayor=num1
else:
    mayor=num2
if mayor<num3:
    mayor=num3
if mayor<num4:
    mayor=num4
elif mayor<num5:
    mayor=num5
print(f"el numero mayor es {mayor}")
