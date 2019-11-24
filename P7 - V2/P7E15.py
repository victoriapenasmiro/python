"""P7E15 VICTORIA PEÑAS
Desarrolla un programa utilizando la metodología “pair programming”,
que nos sirva para gestionar nuestros contactos (la información a
gestionar será el teléfono, nombre, apellido1, apellido2 y correo
electrónico. El programa tendrá un menú, con las siguientes opciones:
añadir contacto, consultar contacto a partir de la clave, consultar
todos los contactos y eliminar contacto. Aprovecha lo que has aprendido
hasta el momento (diccionarios, funciones, procedimientos…)."""

def mostrarMenu(agenda):
    opcion=0
    while opcion!=5:
        print("************MENU************\n" + "Selecciona una opción:\n" +\
        "1.Añadir Contacto\n" + "2.Consultar contacto\n" +\
        "3.Consultar todos los contactos\n" + "4.Eliminar contacto\n"+\
        "5.Salir")
        opcion=int(input("Selecciona la opción que quieres realizar: "))
        while opcion<1 or opcion>5:
            opcion=int(input("La opción introducida no existe, indica otra: "))
        if opcion==1:
            añadirContacto()
        elif opcion==2:
            consultarContacto(agenda)
        elif opcion==3:
            consultarTodos(agenda)
        elif opcion==4:
            eliminarContacto

def añadirContacto():
    global agenda
    global idcont
    contacto=dict()
    contacto["contacto"]=idcont
    contacto["tel"]=int(input("Dime el número de teléfono: "))
    contacto["nombre"]=str(input("Dime el nombre: "))
    contacto["apellido1"]=str(input("Dime el primer apellido: "))
    contacto["apellido2"]=str(input("Dime el segundo apellido: "))
    contacto["email"]=str(input("Dime el email: "))
    agenda.append(contacto)
    #agenda.insert(idcont,contacto)#haciendo un insert en una posicion exacta de la lista. ¿Qué pasa si elimino el elemento dos?
    idcont+=1
    print("¡Contacto añadido!\n")
    return agenda

def consultarContacto(agenda):
    clave=int(input("Qué contacto quieres consultar? Indica código (1,2,3..):"))
    print("Los datos del contacto",clave,"son:")
    #Si el bucle termina y no encuentra el id del contacto, entonces indico
    # al usuario que ese id no existe:
    for j in agenda:
        while clave!=j["contacto"]:
            clave=int(input("El id indicado no es correcto, por favor, indica otro: "))
    for i in agenda:
        if i["contacto"]==clave:
            print("Contacto id:",i["contacto"])
            print("Nombre:",i["nombre"])
            print("Primer apellido:",i["apellido1"])
            print("Segundo apellido:",i["apellido2"])
            print("Correo eletrónico:",i["email"])
            print("-------------")
            break
            """con los siguientes prints podríamos acceder directamente a
            los elementos del diccionario sin un for, con:
            if agenda[clave-1]["contacto"]==clave:
            print("Contacto id:",agenda[clave-1]["contacto"])
            print("nombre:",agenda[clave-1]["nombre"])
            print("Primer apellido:",agenda[clave-1]["apellido1"])
            print("Segundo apellido:",agenda[clave-1]["apellido2"])
            print("Correo eletrónico:",agenda[clave-1]["email"])
            PERO no estaríamos validando el id"""

def consultarTodos(agenda):
    for i in agenda:
        print("Contacto id:",i["contacto"])
        print("nombre:",i["nombre"])
        print("Primer apellido:",i["apellido1"])
        print("Segundo apellido:",i["apellido2"])
        print("Correo eletrónico:",i["email"])
        print("-------------")

def eliminarContacto():
    clave=int(input("Dime el id del contacto que quieres eliminar: "))
    for i in agenda:
        while clave!=i["contacto"]:
            clave=int(input("El id indicado no existe. Indica otro: "))
    #necesito obtener el indice de la lista donde se encuentre el contacto
    for i in agenda:
        if i["contacto"]==clave:
            eliminar i
    
    return

#VARIABLES
agenda=[]
idcont=1
#Empieza el programa
mostrarMenu(agenda)