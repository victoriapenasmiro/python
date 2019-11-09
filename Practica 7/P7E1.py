"""P7E1 VICTORIA PEÑAS
Escribe un programa que pida un texto por pantalla,
este texto lo pase como parámetro a un procedimiento,
y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas."""

def imprimirTexto(t):
    print (t.lower())
    print (t.upper())

texto=str(input("Escribe un texto\n"))
imprimirTexto(texto)
