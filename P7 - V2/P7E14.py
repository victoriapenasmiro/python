"""P7E14 VICTORIA PEÑAS
Aprovechando el potencial de los diccionarios, escribe un programa que llame a
un procedimiento, que recibe como parámetro la fecha en números y devuelve la
fecha con el nombre del mes. Comentario: no es necesario validar si la es
correcta, damos por hecho que lo será. """

def mostrarMes(fecha):
    if fecha["mes"]==1:
        fecha["mes"]="Enero"
    elif fecha["mes"]==2:
        fecha["mes"]="Febrero"
    elif fecha["mes"]==3:
        fecha["mes"]="Marzo"
    elif fecha["mes"]==4:
        fecha["mes"]="Abril"
    elif fecha["mes"]==5:
        fecha["mes"]="Mayo"
    elif fecha["mes"]==6:
        fecha["mes"]="Junio"
    elif fecha["mes"]==7:
        fecha["mes"]="Julio"
    elif fecha["mes"]==8:
        fecha["mes"]="Agosto"
    elif fecha["mes"]==9:
        fecha["mes"]="Septiembre"
    elif fecha["mes"]==10:
        fecha["mes"]="Octubre"
    elif fecha["mes"]==11:
        fecha["mes"]="Noviembre"
    elif fecha["mes"]==12:
        fecha["mes"]="Diciembre"
    print(fecha.get("dia"),"de "+fecha.get("mes")+" del",fecha.get("año"))
fecha=dict()
fecha["dia"]=int(input("Dime el dia: "))
fecha["mes"]=int(input("Dime el mes: "))
fecha["año"]=int(input("Dime el año: "))
mostrarMes(fecha)
