import os
import random

digitos = "1234567890"
numero = ""
muertos = 0
heridos = 0
intento = None
intentos = []
salir = False


"""presentacion de el programa"""

os.system("clear")

print("***************************************************")
print("***************************************************")
print("***************************************************")
print("********  juego de muertos y heridos   ************")
print("********     tienes 10 intentos        ************")
print("********         pulsa enter           ************")
print("***************************************************")
print("***************************************************")
print("***************************************************")

input("dame un numero: ")
#generando el numero a buscar

while len(numero) <= 4:

    digito = random.choice(digitos)
    if digito  not in numero:
        numero += digito


#bucle while principal del juego

while True:

    os.system("clear")

    print("*************************************") 
    print("******MUERTOS    HERIDOS*************") 
    print("*************************************") 
    print("***    NUMERO      -     M - H    ***")
    print("***    ______      -     _____    ***")
    
    #Mostrar al usuario los intentos con las muertes y heridos que este lleva

    for i in range(len(intentos)):
        plantilla = "***    {}            {}  {}    ***"
        print(plantilla.format(intentos[i][0],intentos[i][1],intentos[i][2]))
    print("*                                   *")

    if numero == intento:
        print("     has ganado hasertaste el numero    ")
        print("     encontraste el numero en",len(intentos),"intentos"    )    
        break

    if len(intentos) >= 15:
        print("     perdiste has agotado el numero de intentos    ")
        print("     el nuemero que buscabas era",numero)
        break

    while True:

        intento = str(input("introduce un numero de 4 digitos o la q para salir"))

        if intento == "q":
            salir = True
            break
        elif len(intento) < 4 or len(intento) > 4:
            print("introduse un numero de cuatro cifras")

        elif intento[0] not in digitos or intento[1] not in digitos or intento[2] not in digitos or intentos[3] not in digitos:
            print("introdusca solo numeros de el 0 al 9")

        elif intento[0] == intento[1] or intento[0] == intento[2] or intento[0] == intento[3] or intento[1] == intento[2] or intento[1] == intento[3] or intento[2] == intento[3]:
            print("los numeros que introdusca todos deben de ser distintos no se pueden repetir")

        else:
            break


    if salir == True:
        print("el numero a buscar era", numero)
        break

    for i in range(4):
        if intento[i] == numero:
            if intento[i] == numero[i]:
                muertos += 1
            else:
                heridos += 1        


    intentos.append([intento,muertos,heridos])

    muertos = 0
    heridos = 0
 





