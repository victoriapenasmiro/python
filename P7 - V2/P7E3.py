"""P7E3 VICTORIA PEÑAS
Escribe un programa que lea una frase, y la pase como parámetro
a un procedimiento, y éste debe mostrar la frase con un carácter
en cada línea."""

def mostrarFrase(frase):
    for i in frase:
        print(i)

frase=str(input("Dime una frase: "))
mostrarFrase(frase)
