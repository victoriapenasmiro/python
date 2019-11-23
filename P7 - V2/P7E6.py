"""P7E6 VICTORIA PEÑAS
Escribe un programa que lea el nombre de una persona y un carácter,
le pase estos datos a una función que comprobará si dicho carácter está
en su nombre. El resultado de dicha función lo imprimirá el programa
principal por pantalla."""

def comprobarLetra(texto,letra):
    if letra.upper() or letra.lower() in texto:
        print(f"La letra {letra} está en el nombre que indicas")
    else:
        print(f"La letra {letra} no está en el nombre que indicas")
        
    return

nombre=str(input("Dime un nombre: "))
letra=str(input("Dime la qué letra quieres comprobar si está en el nombre:"))

comprobarLetra(nombre,letra)
