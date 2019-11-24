"""P7E13 VICTORIA PEÑAS
Escribe un programa que le pida al usuario si quiere calcular si un número
es primo con for o con while, por tanto, habrán dos funciones que se
caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks),
o de otra (con while). Ambas funciones devolverá true (si es es primo) o
false (si no es primo). El programa principal informará del resultado. Además,
como mejora puedes calcular el tiempo que tarda en encontrar la solución de una
manera u otra. Comentario: aprovecha el código que tienes ya creado"""
from datetime import datetime
def comprobarPrimoFor(numero):
    global primo
    for i in range(2,numero):
        if numero%i==0:
            primo=False
    end_time=datetime.now()
    if primo==True:
        res="es primo"
    else:
        res="no es primo"
    return print (f"El número {numero} {res}. Calculado en {end_time-start_time}")

def comprobarPrimoWhile(numero):
    global primo
    i=2
    while numero%i!=0:
        res="es primo"
        i+=1
        if numero%i==0 and i==numero:
            res="es primo"
        else:
            primo=False
            res="no es primo"
    if i==numero:#cubre el caso de que digan el numero 2
        res="es primo"
    end_time=datetime.now()
    return print(f"El número {numero} {res}. Calculado en {end_time-start_time}")

numero=int(input("Dime un número: "))
for_while=str(input("Quieres calcularlo con for o con while? "))
start_time=datetime.now()
primo=True
if for_while=="for":
    comprobarPrimoFor(numero)
else:
    comprobarPrimoWhile(numero)