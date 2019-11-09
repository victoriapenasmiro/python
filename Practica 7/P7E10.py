"""P7E10 VICTORIA PEÑAS
Escribe un programa que te pida una palabra o número, pase por parámetro
estos datos a una función, y ésta te diga si es o no palíndroma o
capicúa. El programa principal imprimirá el resultado de la función:
':: significa dame la totalidad\del elemento, el -1 hacia atras' """
def comprobarPalindromo(valor):
    #Otra opción:
    #if secuencia[::-1] == secuencia[:]: --> [::-1] es para leer la variable al revés
     #   return print("es capicua")
    #else:
     #   return print("no es capicua")
    y = 1
    for i in range(len(valor)//2):
        if valor[i]==valor[-y]:
            capicua="es capicua o palíndroma"
        else:
            capicua="no es capicua o palíndroma"
            break
        y+= 1
    return print(capicua)
secuencia=str(input("Dime algo: "))
comprobarPalindromo(secuencia)
