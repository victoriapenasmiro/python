"""P7E6 VICTORIA PEÑAS
Escribe un programa que lea el nombre de una persona y
un carácter, le pase estos datos a una función que comprobará
si dicho carácter está en su nombre. El resultado de
dicha función lo imprimirá el programa principal por pantalla."""
def comprobarLetra(n,c):
    if "n" in "c":
        return print("¡Está!")
    else:
        return print("No está")
nombre=str(input("Dame el nombre de una persona:"))
caracter=str(input("Dime el caracter que quieres comprobar \
si está en el nombre: "))
comprobarLetra(nombre,caracter)
