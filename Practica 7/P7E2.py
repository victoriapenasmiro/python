""" P7E2 VICTORIA PEÑAS
Escribe un programa que lea el nombre y los dos apellidos de una persona
(en tres cadenas de caracteres diferentes), los pase como parámetros a
una función, y ésta debe unirlos y devolver una única cadena. La cadena
final la imprimirá el programa por pantalla."""
def imprimirNombre(a,b,c):
    return a+" "+b+" "+c
nombre=str(input("Tu nombre: "))
apellido1=str(input("Primer apellido: "))
apellido2=str(input("Segundo apellido: "))
print(imprimirNombre(nombre,apellido1,apellido2))
