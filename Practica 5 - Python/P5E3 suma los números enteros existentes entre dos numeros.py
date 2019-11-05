#este programa suma los numeros enteros existentes entre dos numeros
num1=int(input("Dame un número:\n"))
num2=int(input(f"Dame otro número mayor que {num1}:\n"))
res=0
for i in range(num1,num2):
    res=res+i
print (f"La suma desde {num1} a {num2} es: {res+num2}")

