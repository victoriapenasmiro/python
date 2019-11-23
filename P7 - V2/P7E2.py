"""P7E2 VICTORIA PEÑAS
Escribe un programa que lea el nombre y los dos apellidos de una
persona (en tres cadenas de caracteres diferentes), los pase como
parámetros a una función, y ésta debe unirlos y devolver una única
cadena. La cadena final la imprimirá el programa por pantalla."""
def mostrarNombre(nom,ape1,ape2):
    print(nom+" "+ape1+" "+ape2)

nombre=str(input("Dime tu nombre: "))
apellido1=str(input("Dime tu primer apellido: "))
apellido2=str(input("Dime tu segundo apellido: "))

mostrarNombre(nombre,apellido1,apellido2)
