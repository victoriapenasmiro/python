"""P5E12 VICTORIA PEÑAS
Escribe un programa que pida un número y escriba si primo o no"""
calc_primo=int(input("dame un número\n"))
primo=" es primo"
for i in range(2,calc_primo):
    if calc_primo%i==0:
        primo=" no es primo"
print(f"El número {calc_primo}{primo}")
