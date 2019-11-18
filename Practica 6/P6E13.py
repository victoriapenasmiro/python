"""P6E13 VICTORIA PEÑAS
Desarrolla de nuevo el ejercicio de la práctica anterior de los números
primos, con while. Reflexiona y escribe en el propio programa en forma
de comentario, qué opción es mejor y por qué."""
j=2
while num%j!=0:
    primo=" es primo."
    j+=1
    if num%j==0 and j!=num:
        primo=" no es primo."
    print(f"El número {num}{primo}")
    print("=======================")
    print("La opcion while es más rápida en ejecutarse el bucle for\
          puesto que el bucle for recorre TODO el rango de inicio a fin\n\
          y en cambio el while recorre lo \"justo y necesario\" hasta que\
          encuentra un caso que no cumpla la condición. En los casos de los\
          numeros primos el while recorrerá todo el rango y tardará lo mismo\
          que un for pero en los casos de no primos tardará muchisimo menos.")
numero=int(input("Dame el número del que quieres que calcule si es primo: "))
