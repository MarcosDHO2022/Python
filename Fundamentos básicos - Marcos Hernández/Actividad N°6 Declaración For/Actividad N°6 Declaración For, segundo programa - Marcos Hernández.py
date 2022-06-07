#Nombre: Marcos Hernández
#Objectivo: Aprender a usar la estructura repetitiva "For", para repetir unas determinadas
#líneas de código con un límite y condición establecidos.

#Actividad N°6: Declaración For

#2. Realice un programa que genere cualquier tabla de multiplicar:
#a. Utilizar la declaración for.
#b. El usuario debe poder ingresar el valor de la tabla de múltiplicar
#   que desea generar.


#Uso la función de "sleep" (dormir en inglés) de la librería "time" para que el usuario vea
#como se va "actualizando" la tabla de múltiplicar.

from time import sleep

tabladmult = int(input("Ingrese el valor de la tabla de múltiplicar a imprimir: "))
resultado = 0;

print("\nSe imprimirá la tabla del {}:\n".format(tabladmult))

for n in range(0, 11):
    resultado = tabladmult*n
    print("{} X {} = {}". format(tabladmult, n, resultado))
    sleep(1)

print("\nTabla imprimida con éxito.")