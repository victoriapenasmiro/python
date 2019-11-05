"""P5E11 VICTORIA PEÑAS
Escribe un programa que pida un número e imprima todos sus divisores."""
numdivisores=int(input("dame un número\n"))
print ("los divisores de {numdivisores} son:")
for i in range(1,numdivisores+1):
    if numdivisores%i==0:
        print(i)
