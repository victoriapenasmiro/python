"""P7E9 VICTORIA PEÑAS
Escribe un programa que pida dos palabras las pase como parámetro
a un procedimiento y diga si riman o no. Si coinciden las tres
últimas letras tiene que decir que riman. Si coinciden sólo las
dos últimas tiene que decir que riman un poco y si no, que no riman."""
def rimarPalabras (str1,str2):
    if str1[-3:] == str2[-3:]:
        print(f"las palabras {str1} y {str2} riman")
    elif str1[-2:] == str2[-2:]:
        print(f"las palabras {str1} y {str2} riman un poco")
    else:
        print(f"las palabras {str1} y {str2} no riman")
palabra1=str(input("Dime una palabra: "))
palabra2=str(input("Dime otra palabra: "))
rimarPalabras (palabra1,palabra2)
