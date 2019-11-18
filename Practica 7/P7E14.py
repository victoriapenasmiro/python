"""P7E14 VICTORIA PEÑAS
Aprovechando el potencial de los diccionarios, escribe un programa que llame
a un procedimiento, que recibe como parámetro la fecha en números y devuelve
la fecha  con el nombre del mes. Comentario: no es necesario validar si la es
correcta, damos por hecho que lo será."""
def escribirFecha(numdia,nummes,numaño):
    if nummes==1:
        nummes="Enero"
    elif nummes==2:
        nummes="Febrero"
    elif nummes==3:
        nummes="Marzo"
    elif nummes==4:
        nummes="Abril"
    elif nummes==5:
        nummes="Mayo"
    elif nummes==6:
        nummes="Junio"
    elif nummes==7:
        nummes="Julio"
    elif nummes==8:
        nummes="Agosto"
    elif nummes==9:
        nummes="Septiembre"
    elif nummes==10:
        nummes="Octubre"
    elif nummes==11:
        nummes="Noviembre"
    elif nummes==12:
        nummes="Diciembre"
    d={"dia":numdia,"mes":nummes,"año":numaño}
    print("La fecha es",d["dia"],d["mes"],d["año"])
dia=int(input("Dime el día: "))
while dia<1 or dia>31:
    dia=int(input("Dime el día correcto: "))
mes=int(input("Dime el número del mes: "))
while mes<1 or mes>12:
    mes=int(input("Dime un número de mes válido: "))
año=int(input("Dime el año: "))
while año<1000 or año>9999:
    año=int(input("Dime un año válido: "))
escribirFecha(dia,mes,año)
