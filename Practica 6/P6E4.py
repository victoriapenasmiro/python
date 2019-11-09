"""P6E4 VICTORIA PEÑAS
Escribe un programa que te pida dos números, de manera que el segundo
sea mayor que el primero. El programa termina escribiendo los dos
números tal y como se pide:"""
num1=int(input("Escribe un número: "))
num2=int(input(f"Escribe un número mayor que {num1}: "))
while num1>=num2:
    num2=int(input(f"{num2} no es mayor que {num1}. Vuelve \
                   a introducir un número: "))
print(f"Los números que has escrito son {num1} y {num2}")
