2
#Nombre: Marcos Hernández
#Objectivo: Comprender el uso de las condicionales, como el "if", "elif" y "else".

#Actividad N°3: Condicionales

#3. Cree un programa en el que el usuario debe adivinar un número
#en una secuencia de 1 a 10, en el que el número ganador debe ser
#generado de manera aleatoria.

#Si el usuario adivina debe indicarle que acertó, de lo contrario
#debe finalizar el juego.




#Se importa la librería random, para tener resultados aleatorios.
import random

x = 0;
ng = random.randint(1, 10);

#Incluí un while para permitir que el usuario intente varias veces por si se sale del rango
#sin que el programa se termine.

while x!=ng:
    x = int(input("Introduzca el número a adivinar, entre el 1 al 10: "));

    if (x == ng):
        print("Usted acertó el número ganador, el cual es: ", ng);

    elif (x <= 0) or (x >= 10):
        print("El número está fuera del rango. Intente de nuevo...");

    else:
        print("Usted no acertó el número ganador, el cual es:", ng ,". Usted introdujo el:", x);
        break;