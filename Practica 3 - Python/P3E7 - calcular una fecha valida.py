#Este programa valida si la fecha introducida es válida.
dia=int(input("Por favor, introduce el día\n"))
mes=int(input("Por favor, introduce el mes \n"))
ano=int(input("Por favor, introduce el año en formato AAAA\n"))
if dia<1 or dia>31:
    print("El dia introducido no es válido")
elif mes<1 or mes>12:
    print("El mes introducido no es válido")
elif ano<1000 or ano>3000:
    print("El año introducido no es válido")
elif mes==2 and dia==29:
    if ano%4==0 and (ano%100!=0 or ano%400==0):
        print (f"La fecha introducida es válida:{dia}/{mes}/{ano}.")
    else:
        print ("El dia 29 no existe en el mes de febrero del año indicado")
elif mes==4 or mes==6 or mes==9 or mes==11:
    if dia>30:
        print ("El dia indicado no es correcto")
    else:
     print (f"La fecha introducida es válida:{dia}/{mes}/{ano}.")
else:
    print (f"La fecha introducida es válida:{dia}/{mes}/{ano}.")
    
