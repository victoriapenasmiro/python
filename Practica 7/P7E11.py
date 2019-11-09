"""P7E11 VICTORIA PEÑAS
Escribe un programa que te pida una frase, y pase la frase como
parámetro a una función. Ésta debe devolver si es palíndroma o no
, y el programa principal escribirá el resultado por pantalla:"""
def esPalindroma(valor):
    valor1=valor.replace(" ","")#para eliminar espacios. Declaro la
                                #variable valor1 para poder imprimir
                                #la frase con espacios en el return
    if valor1[::-1] == valor1:
        palindroma="es palindroma"
    else:
        palindroma="no es palindroma"
    return print(valor,palindroma)
    #Otra Opcion:
    #y=1
    #for i in range(len(valor)//2):
     #   if valor[i] == valor[-y]:#para referenciar la posicion
                                #concreta hay que declarar la
                                #variable y la posicion entre []
      #      palindroma="es palindroma"
       # else:
        #    palindroma="no es palindroma"
         #   break
        #y+=1
    #return print(valor,palindroma)
frase=str(input("Dime algo: "))
esPalindroma(frase)
