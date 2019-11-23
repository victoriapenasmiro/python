"""P7E1 VICTORIA PEÑAS
Escribe un programa que pida un texto por pantalla, este texto
lo pase como parámetro a un procedimiento, y éste lo imprima
primero todo en minúsculas y luego todo en mayúsculas."""
def convertirTexto(texto):
    print(texto.lower()+"\n"+texto.upper())

texto=str(input("Dime un texto y lo convertiré a mayúsculas y minúsculas:\n"))
convertirTexto(texto)
