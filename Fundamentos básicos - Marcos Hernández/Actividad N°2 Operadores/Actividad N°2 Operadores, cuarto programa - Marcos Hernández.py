#Nombre: Marcos Hernández
#Objectivo: Aprender a usar correctamente los operadores en Python. Ya sea para establecer 
#u evaluar condiciones.


#Actividad N°2: Operadores

#4. Crear un programa en el que el usuario introduzca tres números y
#que el programa muestre en pantalla cuál es el número menor y cuál
#es el mayor respectivamente.

num1 = 0
num2 = 0
num3 = 0

print("En este programa, se calculará cuál es el número mayor y el número menor de tres valores introducidos por el usuario.\n")

num1 = input("Introduzca el primer número: ")
num2 = input("Introduzca el segundo número: ")
num3 = input("Introduzca el tercer número: ")
print("\n")

#Primero, por seguridad, se comprueba si todos los números introducidos son iguales.
if (num1 == num2) and (num2 == num3):
    print("Todos los números tienen el mismo valor de: {}".format(num1))
    quit()


if (num1 == num2) or (num2 == num1) or (num1 == num3) or (num2 == num3):
    #Lista de posibles combinaciones para detectar el número mayor, en caso de que hayan dos números iguales.
    if (num1 > num2) and (num1 > num3): 
        print("Dos números tienen el mismo valor menor de: {}\nHaciendo que el número mayor sea el primer número, cuyo valor es: {}".format(num2, num1))
        quit()

    elif (num2 > num1) and (num2 > num3):
        print("Dos números tienen el mismo valor menor de: {}\nHaciendo que el número mayor sea el segundo número, cuyo valor es: {}".format(num1, num2))
        quit()

    elif (num3 > num1) and (num3 > num2):
        print("Dos números tienen el mismo valor menor de: {}\nHaciendo que el número mayor sea el tercer número, cuyo valor es: {}".format(num1, num3))
        quit()

    #Lista de posibles combinaciones para detectar el número menor, en caso de que hayan dos números iguales.
    elif (num1 < num2) and (num1 < num3): 
        print("Dos números tienen el mismo valor mayor de: {}\nHaciendo que el número menor sea el primer número, cuyo valor es: {}".format(num2, num1))
        quit()

    elif (num2 < num1) and (num2 < num3):
        print("Dos números tienen el mismo valor mayor de: {}\nHaciendo que el número menor sea el segundo número, cuyo valor es: {}".format(num1, num2))
        quit()

    elif (num3 < num1) and (num3 < num2):
        print("Dos números tienen el mismo valor mayor de: {}\nHaciendo que el número menor sea el tercer número, cuyo valor es: {}".format(num1, num3))
        quit()


#Verificar cuál es el número mayor.
if (num1 > num2) and (num1 > num3):
    print("El primer número (", num1,") es el mayor.")

elif (num2 > num1) and (num2 > num3):
    print("El segundo número (", num2,") es el mayor.")

else:
    print("El tercer número (", num3,") es el mayor.")

#Verificar cuál es el número menor.
if (num1 < num2) and (num1 < num3):
    print("El primer número (", num1,") es el menor.")

elif (num2 < num1) and (num2 < num3):
    print("El segundo número (", num2,") es el menor.")

else:
    print("El tercer número (", num3,") es el menor.")

