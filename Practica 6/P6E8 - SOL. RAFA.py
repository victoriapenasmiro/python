num_ini=int(input("Dame un número"))
sumatorio=0
resultado=[]

while sumatorio<num_ini:
    num_a_sumar=int(input("Dime otro número"))
    if num_a_sumar+sumatorio<=num_ini:
        resultado.append(num_a_sumar)
        sumatorio+=num_a_sumar
       
print("El resultado de sumar ",end=" ")
for i in range(len(resultado)-1):
    print(resultado[i],end="+")

print(resultado[-1],"=",num_ini)
