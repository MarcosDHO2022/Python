# Nombres: Andrey Mc Kenzie y Marcos Hernández
# Fecha: 24 de febrero del 2022  / Terminado en el: 28 de febrero del 2022

import random
import time
import os

clear = lambda: os.system('cls')
clear()
juego = str(input(
    "Bienvenido a 'Salva el Jardín'. En este juego, usted tendrá que salvar el jardín recolectando objectos, a base de decisiones.\nEscriba 'iniciar' para comenzar, sino escriba 'Salir' o 'Regresar' para volver al jardín.\n\n>"))
juego = juego.lower()
objectos = []
decision = str
item = str
x = int
x = 0
dinero = 100

def guardar(item):
    objectos.append(item)


if juego == "iniciar":
    #Parte desarrollada por Marcos Hernández
    clear()
    print("Acabas de salir a verificar tu hermoso jardín, pero sorpresa, está hecho un desastre. Las plantas del jardín están muriendo,\nnecesitan que se le quiten las malas hierbas, se le de agua y mantenimiento. Debes de buscar los objetos que encontrarás\nen el camino y evitar realizar malas decisiones; para no perder. Para elegir tu decisión, escribe las palabras que están en comillas.")
    print("\nSe te presentan dos rutas, el 'bosque' o la 'ciudad', que ruta tomaras?\n\n\nObjectos:".format(), *objectos)
    decision = str(input("Acción: "))
    decision = decision.lower()
    if decision == 'bosque':
        time.sleep(2)
        clear()
        print(
            "Te dirigues al bosque. Todo parece tranquilo y relajante, en el camino encuentras una pelota de fútbol.")
        print("\n¿Deseas recogerlo? 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == ('si' or 'sí'):
            print("\nSe guardó la pelota de fútbol.")
            guardar("Pelota de fútbol")

        elif decision == "no":
            print("\nSe decidió no guardar la pelota de fútbol.")

        else:
            print("Se decidió no guardar la pelota de fútbol.")

        while (x == 0):
            time.sleep(2)
            clear()
            print("En el camino, te detienes para observar una particular roca gigante, detras de la roca gigante encuentras una bolsa")
            print("llena de objectos. Entre ellas, está una 'tijera', un 'reloj' y una 'bebida energizante'.")
            print("\n¿Qué objecto deseas agarrar?\n\n\nObjectos:".format(), *objectos)
            decision = str(input("Acción: "))
            decision = decision.lower()
            if decision == "tijera" and "Tijera" not in objectos:
                print("\nSe guardó la tijera.")
                guardar("Tijera")

            elif decision == "reloj" and "Reloj" not in objectos:
                print("\nSe guardó el reloj.")
                guardar("Reloj")

            elif decision == "bebida energizante" and "Bebida energizante" not in objectos:
                print("\nSe guardó la bebida energizante.")
                guardar("Bebida energizante")

            else:
                print("\nNo se especificó el objecto o ya está obtenido.")

            if "Tijera" in objectos and "Reloj" in objectos and "Bebida energizante" in objectos:
                time.sleep(2)
                clear()
                print("Agarraste todos los objectos.")
                time.sleep(2)
                x = 1;
                break

            time.sleep(2)
            clear()
            print("¿Deseas agarrar otro objecto?")
            print("\n¿'si' o 'no'?\n\n\nObjectos:".format(), *objectos)
            decision = str(input("Acción: "))
            decision = decision.lower()

            if decision == ("si" or "sí"):
                x = 0

            elif decision == "no":
                x = 1
                break

            else:
                print("Error al introducir los datos, por favor, especifique mejor.")

        if "Tijera" not in objectos:
            clear()
            print(
                "Te diste cuenta de que no agarraste la tijera, era necesario para continuar con tu objectivo. Te cae un rayo y pierdes...\nIntenta de nuevo.")
            time.sleep(2)
            quit()

        time.sleep(2)
        clear()
        print("Sigues caminando y encuentras un río, y en el río, encuentras un oso gigante. Lastimosamente, estás delante de la vista")
        print("del oso y no te diste cuenta, ya que, estabas mirando el hermoso río. Tienes las siguientes opciones: \n\n'Correr'")

        if "Pelota de fútbol" in objectos:
            print("\n'Tirar pelota de futbol'")

        if "Bebida energizante" in objectos:
            print("\n'Tirar bebida energizante'")

        print("\n¿Qué decides hacer?\n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == "tirar bebida energizante" and "Bebida energizante" in objectos:
            objectos.remove("Bebida energizante")
            clear()
            print("\nTiraste la bebida energizante al oso gigante. Este se queda mirando la botella y...")
            time.sleep(2)
            print("comienza a consumirla.")
            time.sleep(2)

        elif decision == ("tirar pelota de futbol" or "tirar pelota de fútbol") and "Pelota de fútbol" in objectos:
            objectos.remove("Pelota de fútbol")
            clear()
            print("\nTiraste la pelota de futbol al oso gigante. Este se queda mirando la pelota y...")
            time.sleep(2)
            print("comienza a masticarla.")
            time.sleep(2)

        elif decision == "correr":
            clear()
            print("Saliste corriendo del oso y, este, te atrapó. Perdiste... Intenta de nuevo.")
            time.sleep(2)
            quit()

        else:
            clear()
            print(
                "No reaccionaste adecuadamente o no tienes lo necesario para defenderte del oso gigante. Intenta de nuevo.")
            time.sleep(2)
            quit()

        clear()
        clear()
        print("Aprovechas este momento para pasar a través del oso y notas algo curioso detrás de él. ¡Es un insecticida!")
        print("\n¿Deseas agarrar el insecticida? 'si' o 'no'.\n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()

        if decision == ("si" or "sí"):
            clear()
            print("Agarras el insecticida y sales corriendo del oso gigante.")
            guardar("Insecticida")

        elif decision == "no":
            clear()
            print("No te atreviste a agarrar el insecticida y, por lo tanto, te cae un rayo. Perdiste...")
            time.sleep(2)
            quit()

        else:
            clear()
            print("No reaccionaste adecuadamente o no tienes lo necesario para seguir con tu objectivo de salvar el jardín. Intenta de nuevo.")
            time.sleep(2)
            quit()

        time.sleep(2)
        clear()
        print("Una vez has escapado del oso, te das cuenta de que no te faltan muchos objectos para salvar el jardín. El día parece \nque no termina y el sol está más caliente que nunca. En el camino te encuentras una botella de agua. Te preguntas si\nserá buena idea beberte esta botella de agua...")
        print("\n¿Deseas 'beber' la botella de agua o 'guardar' la botella de agua?\n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()

        if decision == "beber":
            time.sleep(2)
            clear()
            print("Decidiste beber la botella de agua. Comienzas a beberla y...")
            time.sleep(2)
            print("te envenenas. El agua no estaba totalmente limpia como para ser consumida. Perdiste... Intenta de nuevo.")
            quit()

        elif decision == "guardar":
            time.sleep(2)
            clear()
            print("Decides guardar la botella de agua. Ya que sabes que te vendrá util para salvar el jardín.")
            guardar("Agua")

        else:
            clear()
            print("Error.")
            quit()

        time.sleep(4)
        clear()
        clear()
        print("Sigues caminando por horas, hasta que te das cuenta que no encuentras más objectos que ayuden a salvar tu jardín...\nAunque, miras a una curioso árbol. Arriba del árbol hay un fertilizante. Tienes las siguientes opciones: \n\n'Trepar'")

        if "Pelota de fútbol" in objectos:
            print("\n'Tirar pelota de futbol'")

        if "Reloj" in objectos:
            print("\n'Tirar reloj'")

        print("\n¿Qué deseas hacer?\n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        
        if decision == "tirar reloj" and "Reloj" in objectos:
            objectos.remove("Reloj")
            clear()
            print("Tiraste el reloj al fertilizante. El reloj se rompe, pero ahora tienes un fertilizante.")
            time.sleep(6)
            guardar("Fertilizante")

        elif decision == ("tirar pelota de futbol" or "tirar pelota de fútbol") and "Pelota de fútbol" in objectos:
            objectos.remove("Pelota de fútbol")
            clear()
            print("Tiraste la pelota de fútbol al fertilizante. Obtienes el fertilizante, pero la pelota de fútbol se va de tu\nvista porque no para de rebotar a altas velocidades.")
            time.sleep(6)
            guardar("Fertilizante") 

        elif decision == "trepar":
            clear()
            print("Comienzas a trepar el árbol. Te cuesta mucho ya que no tienes mucha experiencia, aunque logras conseguir el \nfertilizante y bajarte a salvo.")
            time.sleep(6)
            guardar("Fertilizante")
            clear()

        else:
            clear()
            print("No reaccionaste adecuadamente o no tienes lo necesario para seguir con tu objectivo de salvar el jardín. Intenta de nuevo.")
            time.sleep(2)
            quit()

        clear()
        print("Una vez te das cuenta que ya tienes todos los objectos necesarios para el jardín, abandonas el bosque con una sonrisa y sastifacción.")
        time.sleep(4)



    elif decision == "ciudad":
        #Parte desarrollada por Andrey Mc Kenzie.
        clear()
        print(
            "\nLlegaste a la ciudad, es grande y hay mucha gente ◉◡◉, encontraste una muñeca con aspecto zarrapastroso en un basurero del callejon (⊙.⊙).")
        print("\n¿Deseas guardarlo?, 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == "si":
            print("\nSe guardó la muñeca :).")
            guardar("Muñeca")

        else:
            print("\nSe decidió no guardar la muñeca.")

        time.sleep(2)
        clear()
        print("\nContinuas tu ruta y un hombre te sigue ⊙.sisi☉.")
        print("\n¿Deseas hablar con él? 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == "si":
            time.sleep(2)
            clear()
            print("El hombre con el que hablaste es un coleccionista y te ofrece 100$ por la muñeca 👀.")
            print("\n¿Deseas aceptar el dinero? 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
            decision = str(input("Acción: "))
            decision = decision.lower()
            if decision == "si":
                objectos.remove("Muñeca")
                print("\nTienes $100 dólares [̲̅$̲̅(̲̅ιο0̲̅)̲̅$̲̅] y pierdes la muñeca")
                guardar("$100")
                time.sleep(2)
        else:
            print("No hubo trato")

        time.sleep(2)
        clear()
        print("\nLlegaste a una tienda, hay unas tijeras para jardín.")
        print("\n¿Deseas comprarlo? 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == "si":
            print("\nSe compró la tijera ✂....")
            guardar("Tijera")

        else:
            print(
                "acabas de tomar una mala desición 😔, que pasa >:/\n XD no te culpo eres inperfecto humano, vuelve a jugar :)")
            quit()

        time.sleep(2)
        clear()
        print("\nEncontraste en la tienda un insecticida 'Bloomicite'.")
        print("\n¿Deseas comprarlo? 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == "si":
            print("\nSe compró el insecticida 💕☠🌹🌸✿☠💕")
            guardar("Insecticida")
        else:
            print(
                "acabas de tomar una mala desición 😔, que pasa >:/\n XD no te culpo eres inperfecto humano, vuelve a jugar :)")
            quit()

        time.sleep(2)
        clear()
        print("\nEncontraste en la tienda un fertilizante natural 'Bloomify'.")
        print("\n¿Deseas comprarlo? 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == "si":
            print("\nSe compró el fertilizante 🌻❀❁🏵🐞🐸♻")
            guardar("Fertilizante")
        else:
            print(
                "acabas de tomar una mala desición 😔, que pasa >:/\n XD no te culpo eres inperfecto humano, vuelve a jugar :)")
            quit()

        time.sleep(2)
        clear()
        print("\nEncontraste en la tienda agua💦💧💦")
        print("\n¿Deseas comprarlo? 'si' o 'no'. \n\n\nObjectos:".format(), *objectos)
        decision = str(input("Acción: "))
        decision = decision.lower()
        if decision == "si":
            print("\nSe compró el agua💦")
            guardar("Agua")
            time.sleep(2)

        else:
            print(
                "acabas de tomar una mala desición 😔, que pasa >:/\n XD no te culpo eres inperfecto humano, vuelve a jugar :)")
            quit()

    else:
        clear()
        print("No se especificó el camino, por lo tanto, el personaje no hace nada. Intenta de nuevo.")
        time.sleep(2)
        quit()


    if "$100" in objectos:
        clear()
        print("¡Activaste el minijuego secreto!")
        time.sleep(2)
        clear()
        print("\nEste juego consiste en que, en 10 intentos automáticos y aleatoriamente, podras aumentar o perder el dinero ($100).\nEs a base de suerte (50% de chances de ganar más dinero y un 50% chances de perder dinero).\n")
        print("\n¿Deseas jugar? 'si' o 'no'.\n")
        decision = str(input("Acción: "))
        decision = decision.lower()
        clear()
        if decision == "si":
            for x in range(10):
                aop = random.randint(0, 1)
                if aop == 1:
                    dinero += 10;
                    print("¡Ganas dinero!  Cantidad: ${}". format(dinero))
                    time.sleep(2)
                
                else:
                    dinero -= 10;
                    print("¡Pierdes dinero!  Cantidad: ${}". format(dinero))
                    time.sleep(2)
            
            print("\nGanaste una cantidad final de: ${}". format(dinero))

        elif decision == "no":
            clear()
            print("Se decidió no jugar el minijuego secreto. Procederás al jardín como si nada hubiera pasado.")

        else:
            clear()
            print("No se especificó correctamente, se omitirá el minijuego secreto.")



    time.sleep(4)
    clear()
    print("Bienvenido al jardín nuevamente😸, pudiste recolectar los 4 objetos (Tijera, fertilizante, insecticida y agua)?.")
    print("\n¿'si' o 'no'?\n")
    decision = str(input("Acción: "))
    decision = decision.lower()
    if decision == "si":
        time.sleep(2)
        clear()
        print("Fantástico, ya que tienes los 4 objetos, úsalos y contempla tu jardín ☺️")
        print("¿Deseas usar los 4 objetos 😺? 'si' o 'no'. \n")
        decision = str(input("Acción: "))
        decision = decision.lower()

        if decision == "si":
            time.sleep(2)
            clear()
            print("Contempla tu jardín :D ")
            print("∵ *.•´¸.• * ´✶´♡")
            print("☆ °˛ * ˛☆Π___ *˚☆ *")
            print("˚˛★˛•˚ * / __ / ~⧹。˚˚")
            print("˚ ˛•˛•˚  ｜  田田  ｜門｜ ˚ *")
            print("        🌷╬╬🌷╬╬🌷╬╬🌷╬╬🌷\n")


            print("▄▄▀█▄───▄───────▄")
            print("▀▀▀██──███─────███")
            print("░▄██▀░█████░░░█████░░")
            print("███▀▄███░███░███░███░▄")
            print("▀█████▀░░░▀███▀░░░▀██▀")
            print("████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗        ███████╗░█████╗░██████╗░")
            print("╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝        ██╔════╝██╔══██╗██╔══██╗")
            print("░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░        █████╗░░██║░░██║██████╔╝")
            print("░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗        ██╔══╝░░██║░░██║██╔══██╗")
            print("░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝        ██║░░░░░╚█████╔╝██║░░██║")
            print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░        ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝")
            print("██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗")
            print("██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░")
            print("██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░")
            print("██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗")
            print('██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝')
            print("╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░")

        if decision == "no":
            time.sleep(2)
            clear()
            print("Que mal😥😭, tu jardín no puede crecer, por favor utilice los objetos 😐. Intenta de nuevo.")

    else:
        clear()
        print("Lastima, esto es un Game Over.")
        quit()

elif juego == ("salir" or "regresar"):
    print("Usted salió del juego.")

else:
    print("Error.")