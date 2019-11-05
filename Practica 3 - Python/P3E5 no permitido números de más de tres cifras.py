#Este programa muestra error en números de más de tres dígitos
a=int(input("Por favor, introduce un número de máximo de tres cifras:\n"))
if  a>-999 and a<999:
    print("Número correcto")
else:
    print(f"ERROR: El número {a} tiene más de tres cifras")
