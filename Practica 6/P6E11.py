""" P6E11 VICTORIA PEÑAS
Escribir un programa para jugar a adivinar un número
(el ordenador "piensa" el número y el usuario lo ha de adivinar).
El programa empieza pidiendo entre qué números está el número a adivinar,
se "inventa" un número al azar y luego el usuario va probando valores.
El programa va decidiendo si son demasiado grandes o pequeños."""

import random
import time
random.seed (time.time ())#el time coge la hora una hora es un número
                          #de esa forma genera los números aleatorios en
                          #funcion de la hora. En la nueva version de
                          #python 3.7 ya no se usa
minimo = int (input ("Valor mínimo:"))
maximo = int (input ("Valor máximo:"))
secreto = random.randint (minimo, maximo)
print(f"A ver si adivinas un número entero entre",minimo,"y",maximo)
numero=int(input("Escribe un número: "))
veces=0
while numero !=secreto:
    veces+=1
    if numero>secreto:
        numero=int(input("Demasiado grande! Volver a probar: "))
    else:
        numero=int(input("Demasiado pequeño! Volver a probar: "))
print("Correcto! Lo has intentado",veces,"veces.")        
