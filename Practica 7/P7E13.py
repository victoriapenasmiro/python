"""P7E13 VICTORIA PEÑAS
Escribe un programa que le pida al usuario si quiere calcular si un número
es primo con for o con while, por tanto, habrán dos funciones que se caracteriza
n por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra
(con while). Ambas funciones devolverá true (si es es primo) o false
(si no es primo). El programa principal informará del resultado. Además, como
mejora puedes calcular el tiempo que tarda en encontrar la solución de una
manera u otra. Comentario: aprovecha el código que tienes ya creado"""
from datetime import datetime
def calcularPrimofor (num):
    primo=" es primo"
    for i in range(2,num):
        if num%i==0:
            primo=" no es primo"
    end_time=datetime.now()
    return print(f"El número {num}{primo}. El bucle for ha tardado en ejecutarse: {end_time-start_time}")
def calcularPrimowhile (num):
    j=2
    while num%j!=0:
        primo=" es primo"
        j+=1
        if num%j==0 and j!=num:
            primo=" no es primo"
    end_time=datetime.now()        
    return print(f"El número {num}{primo}. El bucle while ha tardado en ejecutarse: {end_time-start_time}")
numero=int(input("Dame el número del que quieres que calcule si es primo: "))
bucle=str(input("Dime si quieres que ejecute el programa con for o con while: "))
while bucle!="for" and bucle!="while":
    bucle=str(input("Por favor, solo debes indicar \"for\" o \"while\": "))
start_time=datetime.now()
if bucle == "for":
    calcularPrimofor(numero)
elif bucle == "while":
    calcularPrimowhile(numero)
