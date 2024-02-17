import requests
import os
tom = 0
carne = 0
leche = 0
huevos = 0
arroz = 0
salir = False
url = 'https://script.google.com/macros/s/AKfycbyTzuhXzWrotK0jCU6TEHyhB0I1Onc9-i4bZlOv6WqMhu54YITTrbc0etSzNoUI16yclA/exec'

while not salir:
    print("### Bienvenido a Nevera Nancy ###")
    print("## ¿Qué desea ordenar? ##")
    print("1) Tomate [U]     En la orden hay: ",tom)
    print("2) Carne [Lb]     En la orden hay: ",carne)
    print("3) Leche [L]      En la orden hay: ",leche)
    print("4) Huevos [U]     En la orden hay: ",huevos)
    print("5) Arroz [Lb]     En la orden hay: ",arroz)
    print("---- Digite '6' para salir -----")
    op = input("Digite la opcion que desea: ")

    if op == '1':
        tom = input("¿Cuánto tomate (U) desea ordenar?: ")
        os.system("cls")
    elif op == '2':
        carne = input("¿Cuánta carne (Lb) desea ordenar?: ")
        os.system("cls")
    elif op == '3':
        leche = input("¿Cuánta leche (L) desea ordenar?: ")
        os.system("cls")
    elif op == '4':
        huevos = input("¿Cuántos huevos (U) desea ordenar?: ")
        os.system("cls")
    elif op == '5':
        arroz = input("¿Cuánto arroz (Lb) desea ordenar?: ")
        os.system("cls")
    elif op == '6':
        salir = True
    else:
        os.system("cls")
        print("Opción no válida. Por favor, elija una opción válida.")

cargaUtil = {'Tomate': str(tom), 'Lb/Carne': str(carne), 'Litro/Leche': str(leche), 'Huevos': str(huevos), 'Lb/Arroz': str(arroz)}
respuesta = requests.post(url, data=cargaUtil)
print("La informacion se ha enviado a la tienda de repartos")
os.system("pause")

