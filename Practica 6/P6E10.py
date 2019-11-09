""" P6E10 VICTORIA PEÑAS
Escribe un programa que te pida los nombres y notas de alumnos.
Si escribes una nota fuera del intervalo de 0 a 10, el programa
entenderá que no quieres introducir más notas de este alumno. Si
no escribes el nombre, el programa entenderá que no quieres introducir
más alumnos. Nota: La lista en la que se guardan los nombres y notas
tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1,
nota2, etc], [nom3, nota1, nota2, etc], etc]"""
todas_notas=[]
nombre=str(input("Dame un nombre: "))
while nombre!="":
    notas_alu=[]
    notas_alu.append(nombre+":")#Con el "+" concateno cadenas
    nota=int(input("Escribe una nota: "))
    while nota>-1 and nota<11:
        notas_alu.append(nota)
        nota=int(input("Escribe otra nota: "))
    todas_notas.append(notas_alu)
    nombre=str(input("Dame otro nombre: "))
print("Las notas de los alumnos son:")
for i in range(len(todas_notas)):
    for j in range(len(todas_notas[i])):
        #if j!=(len(todas_notas)-1) and j!=(len(todas_notas)):
        if j!=(len(todas_notas[i])-1) and j!=0:    
            print(todas_notas[i][j],end="-")#no consigo posicionar los guiones como corresponde
        else:
            print(todas_notas[i][j],end="")
    print("")
        

    
    
