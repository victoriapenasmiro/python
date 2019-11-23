"""P7E9 VICTORIA PEÑAS
Escribe un programa que pida dos palabras las pase como parámetro
a un procedimiento y diga si riman o no. Si coinciden las tres
últimas letras tiene que decir que riman. Si coinciden sólo las
dos últimas tiene que decir que riman un poco y si no, que no riman."""

def comprobarRima(pal1,pal2):
    if pal1[-3:]==pal2[-3:]:
        print(f"{pal1} rima con {pal2}")
    elif pal1[-2:]==pal2[-2:]:
        print(f"{pal1} rima un poco con {pal2}")
    else:
        print(f"{pal1} no rima con {pal2}")

palabra1=str(input("Dime una palabra: "))
palabra2=str(input("Dime una segunda palabra: "))
comprobarRima(palabra1,palabra2)
