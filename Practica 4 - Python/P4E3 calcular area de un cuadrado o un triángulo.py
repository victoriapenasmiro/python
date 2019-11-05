#calcular area de un cuadrado o un triangulo
base=int(input("Por favor, introduce el tamaño de la base\n"))
altura=int(input("Por favor, introduce el tamaño de la altura\n"))
objeto=str(input("¿Quierés calcular el áerea de un triángulo o de un cuadrado?\n"))
if objeto=="triangulo":
    print(f"El área del triángulo es {(base*altura)/2}")
elif objeto=="cuadrado":
    print(f"El área del cuadrado es {(base*altura)}")
else:
    print("El objeto indicado no es válido")
