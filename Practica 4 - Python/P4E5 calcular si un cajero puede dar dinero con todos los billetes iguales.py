#este programa calcula si un cajero puede dar el dinero en todo billetes del mismo valor
quinientos=500
doscientos=200
cien=100
ciencuenta=50
veinte=20
diez=10
cinco=5
importe=int(input("Por favor, indique cuanto dinero (en euros) desea sacar del cajero\n"))
if importe%quinientos==0:
    print(f"El cajero te devuelve {importe//quinientos} billete/s de {quinientos}.")
elif importe%doscientos==0:
    print(f"El cajero te devuelve {importe//doscientos} billete/s de {doscientos}.")
elif importe%cien==0:
    print(f"El cajero te devuelve {importe//cien} billete/s de {cien}.")
elif importe%ciencuenta==0:
    print(f"El cajero te devuelve {importe//ciencuenta} billete/s de {ciencuenta}.")
elif importe%veinte==0:
    print(f"El cajero te devuelve {importe//veinte} billete/s de {veinte}.")
elif importe%diez==0:
    print(f"El cajero te devuelve {importe//diez} billete/s de {diez}.")
elif importe%cinco==0:
    print(f"El cajero te devuelve {importe//cinco} billete/s de {cinco}.")
else:
    print("El cajero no puede devolver el importe solicitado solo en billetes del mismo valor.")
