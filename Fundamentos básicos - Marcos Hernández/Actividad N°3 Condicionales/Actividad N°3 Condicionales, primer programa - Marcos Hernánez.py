#Nombre: Marcos Hernández
#Objectivo: Comprender el uso de las condicionales, como el "if", "elif" y "else".

#Actividad N°3: Condicionales

#1. Escriba un programa que realice lo siguiente:
#a. Definir la variable x=1+4*3+8/2*4+5**2
#b. Si x es par sumarle 1 a x.
#c. Si es impar sumarle 2 a x.

#Como primer paso, se define la siguiente variable.
x = 1+4*3+8/2*4+5**2


#Se verifica primero si es par para sumarle 1, sino lo es, se le suma 2 con "else".
if x%2==0:
    x += 1
    print("X es par, se le sumó 1: {}". format(x))

else:
    x += 2
    print("X es impar, se le sumó 2: {}". format(x))
