"""P6E12 VICTORIA PEÑAS
Escribir un programa para jugar a adivinar un número (el usuario piensa
un número y el programa lo ha de adivinar). El programa empieza pidiendo
entre qué números está el número a adivinar y luego intenta adivinar de
qué número se trata. El usuario va diciendo si el número que ha dicho el
programa es menor, mayor o igual al que se ha buscado.
Al principio el programa se asegure de que el valor máximo es superior
al valor mínimo.
Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le
decimos "mayor" y al decir "26" le decimos "menor", el programa debe decir
que estamos haciendo trampas y debe dejar de jugar con nosotros."""
import random
minimo=int(input("Valor mínimo:"))
maximo=int(input("Valor máximo:"))
while maximo<=minimo:
    maximo=int(input("El número máximo debe ser mayor al mínimo.\
    Por favor, indica otro: "))
print(f"Piensa un número entre",minimo,"y",maximo,"a ver si lo puedo adivinar")
secreto=random.randint(minimo, maximo)
numero=str(input(f"Es {secreto}?:"))
while numero != "igual":
    if numero=="mayor":
        if minimo==secreto:
            minimo=(secreto+1)
        else:
            minimo=secreto
    elif numero=="menor":
        if maximo==secreto:
            maximo=(secreto-1)          
        else:
            maximo=secreto
    secreto=random.randint(minimo, maximo)
    numero=str(input(f"Es {secreto}?:"))
    if (secreto==minimo and numero=="menor") or (secreto==maximo and numero=="mayor"):
        print("haces trampas, no quiero jugar contigo")
        break
if numero=="igual":
    print("Gracias por jugar!!")
